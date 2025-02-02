import logging
from logging.handlers import RotatingFileHandler

log_path = '/home/elkin/Documents/Python/utilities/bills/terminal/bills.log'

def get_logger(name):
    """Create a logger and the log file related to the root project.

    Args:
        name (string): Name of the app the logger is executed.

    Returns:
        logger: logger to debug some features of the project.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)


    file_h = RotatingFileHandler(log_path, maxBytes=10000, backupCount=3)
    file_h.setLevel(logging.DEBUG)


    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_h.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_h)

    return logger