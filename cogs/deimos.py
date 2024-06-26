import json, os

import loguru
from discord import app_commands
from discord.ext import commands
import discord
from discord.ext.commands import Context
import requests
from dotenv import load_dotenv
from services.agents import user_agent
from services.tools import create_file

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
bot_0 = commands.Bot(command_prefix='!', intents=intents)


class Deimos(commands.Cog, name='Deimos'):
    """
    handles  discord api server api calls using user input
    """

    def __int__(self, bot, channel: discord.TextChannel, member: discord.Member, user: discord.User, stop_loss,
                context: Context):
        load_dotenv()
        self.bot = bot
        self.member = member
        self.user = user
        self.open_api_key = os.getenv("OPENAI_API_KEY")
        self.context = context

    @commands.command(name='start_review')
    async def start_review(self, *args):
        """
        Handle discord bot AI review call
        :return:
        """
        if not self.member:
            _member = self.context.guild.get_member(self.user.id) or await self.context.guild.fetch_member(self.user.id)

        _member = self.member
        await self.context.send(f'Hi {_member.name},\n Welcome to the AI Ethical review Bot, what business '
                                f'requirements are you looking to addres with AI?')
        while args:
            res = user_agent(open_api_key=self.open_api_key, model='gpt-4')
            res.initiate_chat(message=args)
            await self.context.send(f'{res}')


async def setup(bot) -> None:
    await bot.add_cog(Deimos(bot))
