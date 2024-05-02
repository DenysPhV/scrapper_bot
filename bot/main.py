# This example requires the 'message_content' intent.
# src/main.py
# import re
import asyncio
from time import sleep
import discord

from datetime import datetime, timedelta

from discord.ext import commands, tasks
from dataclasses import dataclass

from functions.registration_by_phone import get_chromedriver, enter_verification_code
from db.database_manager import DatabaseManager

# from handlers.bot_handler import register_phone
from handlers.api_handler import get_numbers, get_sms

from log.logger import get_logger
from settings.settings import settings

logger = get_logger()
db_manager = DatabaseManager()

MAX_SESSION_TIME_MINUTES = 2
API_KEY= settings.TEXTCHEST_TOKEN

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    logger.info(f'We have logged in as {bot.user}')
    channel = bot.get_channel(int(settings.CHANNEL_ID))
    await channel.send("Go to start a new session press **>start**")
    
@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
async def break_reminder():
    # Ignore the first execution of this command.
    if break_reminder.current_loop == 0:
        return

    channel = bot.get_channel(int(settings.CHANNEL_ID))
    await channel.send(f"**Take a break!** You've been working for {MAX_SESSION_TIME_MINUTES} minutes.")
  
@bot.command()
async def start(ctx):
    # start to session on the bot
    if session.is_active:
        await ctx.send("Session is already active!")
        return

    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    await ctx.send(f"New session started at {human_readable_time}\n")
    await ctx.send("Please enter:\n"
                   "Command: **>login** - for verification\n"
                   "Command: **>end** - stop to work and reload\n"
                   )

    # start to get phone numbers from API
    phone_numbers = get_numbers(api_key=API_KEY)

    if phone_numbers is None:
        logger.error("No phone numbers available. Check API service or credentials.")
        await ctx.send("Sorry, we're unable to retrieve phone numbers at this time. Please try again later.")
        return

    if phone_numbers is not None:
        logger.info("Got numbers: %s", phone_numbers)

        for phone_number in phone_numbers:
            db_manager.save_phone_number_to_database(phone_number)
            logger.info(f"Saved phone number {phone_number} to the database.")
            # await ctx.send("Phone numbers saved to the database.")

    else:
        await ctx.send("Failed to get phone numbers from API.")
        
    break_reminder.start()

@bot.command(name="stop")
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds=duration))
    break_reminder.stop()
    await ctx.send(f"Session ended after {human_readable_duration}.")


@bot.command()
async def login(ctx):
    api_key=API_KEY
    phone_numbers = db_manager.get_phone_numbers_from_database()

    if phone_numbers: 
        for i, phone_number in enumerate(phone_numbers, 1):
            logger.info(f"{i}. {phone_number}")

        await ctx.send("Please choose somewhere number to login: ")

        try:
           message = await bot.wait_for('message', timeout=60, check=lambda m: m.author == ctx.author)
           choice = int(message.content) - 1

           if 0 <= choice < len(phone_numbers):
                phone_number = phone_numbers[choice][1:]
                await ctx.send(f"You have selected phone: {phone_number}")

                driver = get_chromedriver()
                driver.get("https://go.seated.com/notifications/login")
                driver.type('input[placeholder="Phone Number"]', phone_number)
                driver.click('button[type="submit"]', timeout=10)

                # Ожидание SMS
                await asyncio.sleep(30)  # Даем время для получения SMS
                sms_data = get_sms(api_key, phone_number)
                # logger.info(f"Received SMS data: {sms_data}")
                
                if sms_data:
                    for sms in sms_data:
                        if 'msg' in sms and "Your Seated verification number is:" in sms['msg']:
                            verification_code = sms['msg'].split(":")[1].strip()
                            await ctx.send(f"Verification code: {verification_code}")

                            # Ввод кода на сайт
                            enter_verification_code(driver, verification_code)
                            await ctx.send("You have been logged in successfully.")
                            return verification_code
                else:
                    await ctx.send("Sorry, we're unable to retrieve SMS messages at this time. Please try again later.")  
                    
                driver.quit()
                    
           else:
                await ctx.send("Invalid choice. Please choose a number from the list.")      

        except asyncio.TimeoutError:
           await ctx.send("Timeout: No confirmation code received.")

    else:
        await ctx.send("Failed to get phone numbers.")   

def run_bot():
    bot.run(settings.DISCORD_TOKEN)    

if __name__ == "__main__":
  run_bot() # start the bot
#   asyncio.run(run_bot())


