import logging
import sys

from settings.settings import settings

logger = None


def get_logger():
    global logger
    if logger:
        return logger

    logger = logging.getLogger(settings.LOGGER_NAME)
    formatter = logging.Formatter(fmt="%(levelname)s: (%(asctime)s)%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger.setLevel(logging.DEBUG)
    log_option = settings.LOG_OPTION

    if log_option in [1, 2]:
        fh_file = logging.FileHandler("scraper_bot.log")
        fh_file.setLevel(logging.INFO)
        fh_file.setFormatter(formatter)
        logger.addHandler(fh_file)

    if log_option in [0, 2]:
        fh_stream = logging.StreamHandler(sys.stdout)
        fh_stream.setLevel(logging.DEBUG)
        fh_stream.setFormatter(formatter)
        logger.addHandler(fh_stream)
        
    return logger
