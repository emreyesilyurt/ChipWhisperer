#!/usr/bin/env python3
"""
Helper - Utility functions for ChipWhisperer PDF Extractor
"""

import re
import os
from pathlib import Path

def clean_text(text):
    """
    Basic text cleaning function
    
    Args:
        text (str): Text to clean
        
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
        
    # Remove page markers added during extraction if present
    text = re.sub(r'\n\n--- PAGE \d+ ---\n\n', '\n\n', text)
    
    # Remove excessive whitespace but preserve paragraph breaks
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Replace tabs with spaces
    text = text.replace('\t', '    ')
    
    return text.strip()

def ensure_directory(directory_path):
    """
    Ensure a directory exists, creating it if necessary
    
    Args:
        directory_path (str): Path to directory
        
    Returns:
        bool: True if directory exists or was created, False otherwise
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        return True
    except Exception:
        return False

def get_output_path(input_path, output_dir=None, suffix="_extracted"):
    """
    Generate an output file path based on the input path
    
    Args:
        input_path (str): Path to input file
        output_dir (str, optional): Directory for output file. Defaults to None.
        suffix (str, optional): Suffix to add to filename. Defaults to "_extracted".
        
    Returns:
        str: Output file path
    """
    input_path = Path(input_path)
    
    if output_dir:
        output_dir = Path(output_dir)
        ensure_directory(output_dir)
        return str(output_dir / f"{input_path.stem}{suffix}.txt")
    else:
        return str(input_path.with_stem(f"{input_path.stem}{suffix}").with_suffix(".txt"))