#!/usr/bin/env python3
"""
PDF Reader - Handles PDF classification (text vs. image-based)
"""

import fitz  # PyMuPDF
from utils.logger import log_info, log_error

def classify_pdf(pdf_path):
    """
    Classify a PDF as either text-based or image-based.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: 'text' if the PDF contains selectable text, 'image' otherwise
    """
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        text_pages = 0
        image_pages = 0
        
        for page_num, page in enumerate(doc):
            # Get text content from page
            text = page.get_text().strip()
            
            # Get image count on page
            image_list = page.get_images(full=True)
            
            # Check if page has meaningful text
            if len(text) > 50:  # Arbitrary threshold to ignore pages with minimal text
                text_pages += 1
                log_info(f"Page {page_num + 1}: Text-based (text length: {len(text)})")
            else:
                # If minimal text but has images, likely an image-based page
                if len(image_list) > 0:
                    image_pages += 1
                    log_info(f"Page {page_num + 1}: Image-based ({len(image_list)} images)")
                else:
                    # No text and no images - might be a blank page or form
                    log_info(f"Page {page_num + 1}: Unknown (minimal text, no images)")
        
        # If more than 50% of pages are text-based, classify as text
        if text_pages > total_pages * 0.5:
            log_info(f"PDF classified as text-based ({text_pages}/{total_pages} pages with text)")
            return "text"
        else:
            log_info(f"PDF classified as image-based ({image_pages}/{total_pages} pages with images)")
            return "image"
            
    except Exception as e:
        log_error(f"Error classifying PDF: {e}")
        # Default to image-based if classification fails
        return "image"

def get_pdf_metadata(pdf_path):
    """
    Extract metadata from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        dict: PDF metadata
    """
    try:
        doc = fitz.open(pdf_path)
        metadata = doc.metadata
        
        # Add additional metadata
        metadata['page_count'] = len(doc)
        
        return metadata
    except Exception as e:
        log_error(f"Error extracting PDF metadata: {e}")
        return {}