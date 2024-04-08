import logging
import os

import discord
from discord.ext import commands

# Import config and logging functions
from config_loader.config_manager import config
from logger_setup.logger_config import setup_logging

# Import setup functions from command and event modules
from bot_commands.general_commands import setup as setup_general_commands
from bot_events.general_events import setup as setup_general_events

bot_dir = os.path.abspath(os.path.dirname(__file__))

setup_logging(f'{bot_dir}/log/discord-bot.log')
bot_logger = logging.getLogger()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

setup_general_events(bot)
setup_general_commands(bot)

bot.run(config.discord_params['DISCORD_TOKEN'])
