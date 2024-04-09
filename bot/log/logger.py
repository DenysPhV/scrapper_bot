import logging
import sys

from settings.settings import settings

logger = None


def get_logger():
    logger = logging.getLogger(settings.LOGGER_NAME)
    logger.setLevel(settings.LOG_OPTION)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
