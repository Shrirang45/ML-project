import logging  # Used to record events, errors, and messages in a log file
import os       # Used to work with files and folders
from datetime import datetime  # Used to get the current date and time


# Create a unique log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Create the path for the 'logs' folder inside the current working directory
logs_path = os.path.join(os.getcwd(), "logs")


# Create the 'logs' folder if it doesn't already exist
# exist_ok=True prevents an error if the folder already exists
os.makedirs(logs_path, exist_ok=True)


# Create the complete path of the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# Configure the logging system
logging.basicConfig(

    # Log messages will be stored in this file
    filename=LOG_FILE_PATH,

    # Format of each log message
    # %(asctime)s  -> Date and time
    # %(lineno)d   -> Line number where logging was called
    # %(name)s     -> Logger name
    # %(levelname)s-> Log level (INFO, ERROR, etc.)
    # %(message)s  -> Actual log message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    # Minimum log level to record
    # INFO means INFO, WARNING, ERROR, and CRITICAL messages will be saved
    level=logging.INFO
)

