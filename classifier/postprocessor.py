#!/usr/bin/env python3
"""
Postprocessor - Text processing after extraction
"""

import re

def format_extracted_text(text):
    """
    Format and clean extracted text
    
    Args:
        text (str): Raw extracted text
        
    Returns:
        str: Formatted text
    """
    if not text:
        return ""
    
    # Fix common OCR/extraction issues
    
    # Remove repeated punctuation
    text = re.sub(r'([.,;:!?])\1+', r'\1', text)
    
    # Fix broken sentences (lowercase letter followed by capital)
    text = re.sub(r'(\w)\.(\s+)([a-z])', r'\1. \3', text)
    
    # Fix spacing after punctuation
    text = re.sub(r'(\w)([.,;:!?])(\w)', r'\1\2 \3', text)
    
    # Fix broken hyphenated words at line breaks
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    
    # Fix common OCR errors
    ocr_fixes = {
        'tbe': 'the',
        'tbat': 'that',
        'bave': 'have',
        'witb': 'with',
        'tbe ': 'the ',
        ' tbe ': ' the ',
        'Tbe ': 'The ',
    }
    
    for error, correction in ocr_fixes.items():
        text = text.replace(error, correction)
    
    # Normalize whitespace (single spaces between words, double newlines between paragraphs)
    text = re.sub(r'\s+', ' ', text)  # Replace all whitespace with single space
    text = re.sub(r'(\. |\? |! )', r'\1\n\n', text)  # Add paragraph breaks after sentences
    
    return text.strip()

def extract_sections(text, section_headings=None):
    """
    Extract sections from text based on headings
    
    Args:
        text (str): Formatted text
        section_headings (list, optional): List of section headings to look for. 
                                          Defaults to common document headings.
        
    Returns:
        dict: Dictionary of section headings and their content
    """
    if not text:
        return {}
        
    if section_headings is None:
        # Default section headings to look for
        section_headings = [
            'Abstract', 'Introduction', 'Background', 'Methods', 'Methodology',
            'Results', 'Discussion', 'Conclusion', 'References', 'Appendix'
        ]
    
    sections = {}
    current_section = 'Default'
    sections[current_section] = []
    
    for line in text.split('\n'):
        # Check if line is a section heading
        line_clean = line.strip().lower()
        
        matched_heading = None
        for heading in section_headings:
            if heading.lower() == line_clean or line_clean.startswith(heading.lower() + ':'):
                matched_heading = heading
                break
        
        if matched_heading:
            current_section = matched_heading
            sections[current_section] = []
        else:
            sections[current_section].append(line)
    
    # Convert lists to strings
    for section in sections:
        sections[section] = '\n'.join(sections[section])
    
    return sections