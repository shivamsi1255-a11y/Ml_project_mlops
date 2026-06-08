import sys
from src.mlproject.logger import logging


class CustomException(Exception):
    """
    Custom exception class for handling project-specific errors.
    """
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        exc_type, exc_value, exc_traceback = error_detail.exc_info()
        
        self.lineno = exc_traceback.tb_lineno if exc_traceback else None
        self.file_name = exc_traceback.tb_frame.f_code.co_filename if exc_traceback else None

    def __str__(self):
        return f"Error occurred in python script name [{self.file_name}] at line number [{self.lineno}] with error message: [{str(self.error_message)}]"


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Dividing by zero")
        raise CustomException(e, sys)
