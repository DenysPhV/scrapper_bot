import logging

from settings.settings import settings

def get_logger():
    logger = logging.getLogger(settings.LOGGER_NAME)
    logger.setLevel(settings.LOG_OPTION)

    if not logger.handlers:
       formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
       console_handler = logging.StreamHandler()
       console_handler.setFormatter(formatter)
       logger.addHandler(console_handler)

    return logger
