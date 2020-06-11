import os
import urllib.request, json
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
QUOTE_URL = os.getenv('QUOTE_URL')

bot = commands.Bot(command_prefix='!')

@bot.command(name='q', help='Responds with a random quote')
async def nine_nine(ctx):

    req = urllib.request.Request(
        QUOTE_URL, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    # Response parsing to get the quote
    response = urllib.request.urlopen(req)
    values = json.load(response)
    response = values['quote']

    await ctx.send(response)

bot.run(TOKEN)
