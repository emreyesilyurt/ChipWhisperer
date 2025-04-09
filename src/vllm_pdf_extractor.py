#!/usr/bin/env python3
"""
ChipWhisperer PDF Extractor - Core Extraction Logic
Handles text extraction using either GPT-4V (for image-based PDFs) or Llama 3 (for text-based PDFs)
"""

import base64
import os
import requests
import json
from io import BytesIO

import fitz  # PyMuPDF
from openai import OpenAI
from utils.logger import log_info, log_error

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def extract_pdf_text(pdf_path, use_vllm=True, vllm_model="gpt-4-vision-preview", llama3_model="llama3"):
    """
    Extract text from a PDF using the appropriate model
    
    Args:
        pdf_path (str): Path to the PDF file
        use_vllm (bool): If True, use GPT-4V, otherwise use Llama 3
        vllm_model (str): The GPT-4V model name to use
        llama3_model (str): The Llama 3 model to use via Ollama
        
    Returns:
        str: The extracted text
    """
    if use_vllm:
        return extract_text_with_gpt4v(pdf_path, model=vllm_model)
    else:
        return extract_text_with_llama3(pdf_path, model=llama3_model)

def extract_text_with_gpt4v(pdf_path, model="gpt-4-vision-preview"):
    """
    Use GPT-4V to extract text from image-based PDFs.
    
    Args:
        pdf_path (str): Path to the PDF file
        model (str): The GPT-4V model to use
        
    Returns:
        str: The extracted text
    """
    try:
        doc = fitz.open(pdf_path)
        extracted_text = ""
        
        for page_num, page in enumerate(doc):
            log_info(f"Processing page {page_num + 1}/{len(doc)} with GPT-4V")
            
            # Render page to PNG image
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x scale for better quality
            img_data = pix.tobytes("png")
            
            # Encode image data for API
            base64_image = base64.b64encode(img_data).decode('utf-8')
            
            # Prepare prompt for GPT-4V
            prompt = """
            Extract ALL text content from this document page. 
            Maintain the original text structure and formatting as much as possible.
            Include headers, paragraphs, lists, and any other textual elements.
            Do not summarize or interpret the content, just extract the text verbatim.
            """
            
            # Call GPT-4V API
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a document OCR assistant that precisely extracts text from images."},
                    {"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                    ]}
                ],
                max_tokens=4096
            )
            
            page_text = response.choices[0].message.content
            extracted_text += f"\n\n--- PAGE {page_num + 1} ---\n\n{page_text}"
        
        return extracted_text
        
    except Exception as e:
        log_error(f"Error in GPT-4V extraction: {e}")
        raise

def extract_text_with_llama3(pdf_path, model="llama3"):
    """
    Use Llama 3 to extract and process text from text-based PDFs.
    
    Args:
        pdf_path (str): Path to the PDF file
        model (str): The Llama 3 model to use via Ollama
        
    Returns:
        str: The extracted text
    """
    try:
        # Extract raw text from PDF
        doc = fitz.open(pdf_path)
        full_text = ""
        
        for page_num, page in enumerate(doc):
            log_info(f"Extracting text from page {page_num + 1}/{len(doc)}")
            page_text = page.get_text("text")
            full_text += f"\n\n--- PAGE {page_num + 1} ---\n\n{page_text}"
        
        # If text is too long for Llama, we'll process page by page or with chunking
        if len(full_text) > 32000:  # Approximate token limit for safety
            log_info("Text is too long, truncating to first 32000 characters")
            full_text = full_text[:32000]
        
        # Call Llama 3 via Ollama API
        log_info(f"Processing extracted text with Llama 3 ({model})")
        
        try:
            # Ollama API endpoint
            ollama_url = "http://localhost:11434/api/chat"
            
            response = requests.post(
                ollama_url,
                json={
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are a document processing assistant. Clean up and structure the extracted text without losing any information."},
                        {"role": "user", "content": f"Process the following PDF text to create a clean, well-structured version that preserves all content and formatting:\n\n{full_text}"}
                    ],
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["message"]["content"]
            else:
                log_error(f"Ollama API error: {response.status_code} - {response.text}")
                # Fallback to returning the raw text if Llama processing fails
                return full_text
                
        except Exception as e:
            log_error(f"Error calling Llama 3 via Ollama: {e}")
            # Fallback to returning the raw text
            return full_text
    
    except Exception as e:
        log_error(f"Error in Llama 3 extraction: {e}")
        raise