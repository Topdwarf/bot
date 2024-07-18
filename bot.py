import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Завантажуємо змінні середовища з файлу .env
load_dotenv()

# Витягнемо токен бота зі змінних середовища
BOT_TOKEN = os.getenv('MTI2Mjg1MTI2MDg4MTY5ODg4OA.G2Oete.wlJN6xH_0dkLo4HDW8mxnFNPe77WZl6rgn0SCc')

# Ініціалізуємо бота
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Логуємо подію входу бота в мережу
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Додаємо команду !hello, яка відправляє повідомлення "Привіт, світ!"
@bot.command()
async def hello(ctx):
    await ctx.send('Привіт, світ!')

# Запускаємо бота
bot.run('MTI2Mjg1MTI2MDg4MTY5ODg4OA.G2Oete.wlJN6xH_0dkLo4HDW8mxnFNPe77WZl6rgn0SCc')
