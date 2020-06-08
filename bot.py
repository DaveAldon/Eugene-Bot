import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='poop', help='When ya gotta dump')
async def poop(ctx):
    poop_ascii = ["""
░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
░░█░░░▐░░░░░░░░▄░█░░░░░
░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
░░▐█▐░░░▀░░░░░░▐░█▄▄░░░
░░▀▀░░▄▄▄▄▄░░░░▐▄▄▄▀░░░
░░░░░░░░░░░░░░░░░░░░░░░
    """]
    response = random.choice(poop_ascii)
    await ctx.send(response)

bot.run(TOKEN)
