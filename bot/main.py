# This example requires the 'message_content' intent.
import asyncio

from settings.settings import settings
from handlers.api_handler import get_numbers, get_sms
from handlers.bot_handler import run_bot

from log.logger import get_logger

TEXTCHEST_TOKEN = settings.TEXTCHEST_TOKEN

logger = get_logger()

def main():
    numbers = get_numbers(api_key=TEXTCHEST_TOKEN)
    if numbers:
        logger.info("Got numbers: %s", numbers)
    else:
        logger.error("Failed to get numbers.")

    for number in numbers:
        print(number)
        message = get_sms(TEXTCHEST_TOKEN, number)
        if message:
            logger.info("Got SMS for number %s: %s", number, message)
        else:
            logger.error("Failed to get SMS for number %s.", number)

    

if __name__ == "__main__":
  main()
  run_bot() # start the bot


