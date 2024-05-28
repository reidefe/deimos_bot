import discord
import os

import loguru
from dotenv import load_dotenv
from discord.ext import commands
import discord
from tools import split_text
from discord.ext.commands import Context
# from services.agents import user_agent, user_chat
from agents import user_agent, user_chat, anthropic_chat, groq_chat, groq_intro_chat

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guild_messages = True
intents.dm_messages = True
intents.messages = True

client = discord.Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_message(message):
    """
    Handles chat with user directly
    :params
    :message:
    """
    if message.author == client.user:
        return
    if message.content.startswith('!start_review'):
        question = message.content
        r = question.split(' ', 1)
        res = await groq_chat(api_key=os.getenv('GROQ_KEY'), prompt=f'{r}')
        if res.__len__() > 2000:
            substrings = split_text(input_string=res)
            for string in substrings:
                await message.channel.send(f' {string}')
        await message.channel.send(f' {res}')
        return

    res = await groq_intro_chat(api_key=os.getenv('GROQ_KEY'), prompt=f'{message.content}')

    await message.channel.send(f' {res} \n write !start_review to commence review')


@client.event
async def on_guild_join(guild):
    """
    Send a message to the guild/server
    """
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embedHi = discord.Embed(
                title="Thanks for adding me!",
                description="AI bot that performs business review forethical AI implementation",
                colour=discord.Colour.red())
            embedHi.set_thumbnail(
                url="https://cdn.pixabay.com/photo/2017/12/13/16/01/brain-3017071_1280.png"
            )
            embedHi.set_image(url="image url")
            embedHi.set_footer(
                text="© Reidefe - The Greate - AI bot for reviews")
            await channel.send(embed=embedHi)
        break


load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))
