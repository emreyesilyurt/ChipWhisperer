#!/usr/bin/env python3
"""
ChipWhisperer PDF Extractor - Main Entry Point
Intelligently extracts text from PDFs using either GPT-4V or Llama 3
"""

import os
import argparse
import json
from pathlib import Path

from utils.logger import log_info, log_error
from utils.pdf_reader import classify_pdf
from utils.helper import clean_text
from src.vllm_pdf_extractor import extract_pdf_text
from classifier.postprocessor import format_extracted_text

def load_config():
    """Load configuration from config file"""
    config_path = Path(__file__).parent.parent / "configs" / "config.json"
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        log_error(f"Error loading configuration: {e}")
        return {
            "vllm_model": "gpt-4-vision-preview",
            "llama3_model": "llama3"
        }

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Extract text from PDF using appropriate LLM')
    parser.add_argument('--pdf', type=str, default="examples/sample.pdf", 
                        help='Path to the PDF file')
    parser.add_argument('--output', type=str, help='Path to save extracted text')
    parser.add_argument('--force-vllm', action='store_true', 
                        help='Force using GPT-4V regardless of PDF type')
    parser.add_argument('--force-llama', action='store_true', 
                        help='Force using Llama 3 regardless of PDF type')
    args = parser.parse_args()
    
    pdf_path = args.pdf
    
    # Check if file exists
    if not os.path.exists(pdf_path):
        log_error(f"PDF file not found: {pdf_path}")
        return
    
    # Load configuration
    config = load_config()
    log_info(f"Using configuration: {config}")
    
    # Determine PDF type and LLM to use
    use_vllm = True
    if args.force_vllm:
        log_info("Forcing GPT-4V for extraction as requested")
        use_vllm = True
    elif args.force_llama:
        log_info("Forcing Llama 3 for extraction as requested")
        use_vllm = False
    else:
        pdf_type = classify_pdf(pdf_path)
        log_info(f"PDF classified as: {pdf_type}")
        use_vllm = (pdf_type == "image")
    
    # Extract text using appropriate method
    try:
        log_info(f"Extracting text from {pdf_path} using {'GPT-4V' if use_vllm else 'Llama 3'}")
        extracted_text = extract_pdf_text(
            pdf_path, 
            use_vllm=use_vllm, 
            vllm_model=config["vllm_model"],
            llama3_model=config["llama3_model"]
        )
        
        # Post-process the extracted text
        processed_text = format_extracted_text(clean_text(extracted_text))
        
        # Output results
        if args.output:
            with open(args.output, 'w') as f:
                f.write(processed_text)
            log_info(f"Extracted text saved to {args.output}")
        else:
            print("\n--- EXTRACTED TEXT ---\n")
            print(processed_text)
            print("\n----------------------\n")
        
        log_info("Text extraction completed successfully")
        
    except Exception as e:
        log_error(f"Error during text extraction: {e}")

if __name__ == "__main__":
    main()
