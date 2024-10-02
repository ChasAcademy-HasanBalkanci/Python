import logging
from datetime import datetime

def setup_logging():
    logging.basicConfig(filename=f"logs_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.log",
                        level=logging.INFO, format='%(asctime)s - %(message)s')

def log_event(event):
    logging.info(event)
