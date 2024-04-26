# bot/handlers/bot_handler.py
from settings.settings import settings
from handlers.api_handler import get_numbers

from functions.registration_by_phone import register_by_phone

api_key = settings.TEXTCHEST_TOKEN

async def start_registration(ctx):
    phone_numbers = await get_numbers(api_key)
    await ctx.send("Please choose a phone number to register:\n")
    for i, number in enumerate(phone_numbers, 1):
        await ctx.send(f"{i}. {number}")
    await ctx.send("Enter the number index to register (e.g., '>reg 1')")

async def register_phone(ctx, phone_index):
    phone_numbers = await get_numbers(api_key)
    if phone_index < 1 or phone_index > len(phone_numbers):
        await ctx.send("Invalid phone number index.")
        return
    selected_phone = phone_numbers[phone_index - 1]
    success = await register_by_phone(selected_phone)
    if success:
        await ctx.send("Registration successful.")
    else:
        await ctx.send("Failed to register the phone number.")

