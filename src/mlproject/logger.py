import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Create log file name with timestamp
log_file = os.path.join(log_dir, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Get logger instance
logging = logging.getLogger(__name__)
