"""
Logger Module
Centralized logging configuration for JARVIS
"""

import logging
import os
from datetime import datetime
from config.settings import LOG_LEVEL, LOG_FILE

def setup_logger():
    """Setup centralized logging"""
    
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()  # Also log to console
        ]
    )
    
    logger = logging.getLogger('JARVIS')
    logger.info("="*50)
    logger.info(f"JARVIS logging initialized at {datetime.now()}")
    logger.info("="*50)
    
    return logger
