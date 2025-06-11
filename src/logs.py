import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
LOG_FILE = f"{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log"  # Format current date and time
log_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

os.makedirs(log_path, exist_ok=True)  # Create logs directory if it doesn't exist
log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s  %(name)s %(lineno)d %(threadName)s- %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if  __name__ == "__main__":
    # Set up console logging
    logging.info("Logging setup complete. Logging to console and file.")




