from datetime import datetime
import sys
import logging


def setup_logging():
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler("log1" + datetime.now().strftime('%Y-%m-%d.log'))
    log_format = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)
    c_handler.setLevel((logging.DEBUG))

    # Define LOGGER
    logger = logging.getLogger('APP')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger
