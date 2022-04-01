
# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = "OTU5NDY5MzkwODMzNzkwOTg2.YkcVgA.HxjKGywEOdvM4g60l0w2rxMSe8M"
GUILD = "917506579048329308"
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)