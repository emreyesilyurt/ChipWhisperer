#!/usr/bin/env python3
"""
Logger - Logging utilities for ChipWhisperer PDF Extractor
"""

import logging
import os
from datetime import datetime
from pathlib import Path

# Create logs directory if it doesn't exist
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Generate log filename with timestamp
log_filename = log_dir / f"chipwhisperer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()  # Also log to console
    ]
)

# Create logger
logger = logging.getLogger("chipwhisperer")

def log_info(message):
    """Log an info message"""
    logger.info(message)

def log_error(message):
    """Log an error message"""
    logger.error(message)

def log_warning(message):
    """Log a warning message"""
    logger.warning(message)

def log_debug(message):
    """Log a debug message"""
    logger.debug(message)