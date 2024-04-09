# src/bot_handler.py
import discord
import re

from datetime import datetime

from discord.ext import commands, tasks
from dataclasses import dataclass

from bot.settings.settings import settings
from bot.scraper import register_user
from bot.db.execute import insert_registration_data

MAX_SESSION_TIME_MINUTES = 2

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(int(settings.CHANNEL_ID))
    await channel.send("Go to start a new session press '>start'")

@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
async def break_reminder():
    # Ignore the first execution of this command.
    if break_reminder.current_loop == 0:
        return

    channel = bot.get_channel(int(settings.CHANNEL_ID))
    await channel.send(f"**Take a break!** You've been working for {MAX_SESSION_TIME_MINUTES} minutes.")

@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("Session is already active!")
        return

    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    break_reminder.start()
    await ctx.send(f"New session started at {human_readable_time}\n")
    await ctx.send("If you want to registration on the site, use the command \n "
                   "**>registration** "
                   "<**your email**> "
                   "<**password min 12 simbols**> "
                   "<**confirm password**>")

@bot.command()
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
async def registration(ctx, email, password, confirm_password):
    success = register_user(email, password, confirm_password)
    if success:
        await ctx.send("Successfully registered!")
    await ctx.send("Registration failed. Please try again.")

@bot.command()
async def register(ctx, email, first_name, last_name, phone_number):
    # Проверка формата номера телефона
    if not re.match(r'^\+?\d{10,15}$', phone_number):
        await ctx.send("Invalid phone number format.")
        return
    
    # Отправка номера телефона на сервис через API
    success = send_data_to_service(email, first_name, last_name, phone_number)
    if success:
        insert_registration_data(email, first_name, last_name, phone_number)
        await ctx.send("Registration successful!")
    else:
        await ctx.send("Failed to register. Please try again.")


# TODO Функция для отправки данных на сервис через API
def send_data_to_service(email, first_name, last_name, phone_number):
    # TODO Ваша логика отправки данных на сервис через API
    pass



def run_bot():
    bot.run(settings.DISCORD_TOKEN)