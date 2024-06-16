import logging
import os

import discord
from discord.ext import commands

from bot_commands.general_commands import setup as setup_general_commands
from bot_events.general_events import setup as setup_general_events
from config_loader.appconfig import AppConfig
from logger_setup.logger_config import setup_logging


bot_dir = os.path.abspath(os.path.dirname(__file__))

setup_logging(f'{bot_dir}/log/discord-bot.log')
bot_logger = logging.getLogger()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

config = AppConfig(bot_dir)
setup_general_commands(bot)
setup_general_events(bot, config)


bot.run(config.discord_params['DISCORD_TOKEN'])
