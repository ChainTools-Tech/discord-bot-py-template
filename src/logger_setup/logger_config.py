import logging
import sys


def setup_logging(log_file):
    """
    Sets up the logging configuration, ensuring no duplicate handlers.
    """
    # Define log formatter
    log_formatter = logging.Formatter('[%(asctime)s] [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Get the root logger
    root_logger = logging.getLogger()
    # Remove all existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Configure file handler
    file_handler = logging.FileHandler(filename=log_file, encoding='utf-8', mode='w')
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    # Configure console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    root_logger.setLevel(logging.DEBUG)