import logging
import discord
from discord.ext import commands

from config_loader.config_manager import config

# Retrieve the root logger or a named logger if you prefer
bot_logger = logging.getLogger(__name__)

class GeneralEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guild = discord.utils.get(self.bot.guilds, name=config.discord_params['DISCORD_GUILD'])  # Adjust as necessary
        bot_logger.info(
            f'{self.bot.user.name} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        members = '\n - '.join([member.name for member in guild.members])
        bot_logger.info(f'Guild members:\n - {members}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "help":
            response = "Testing 1 2 3"
            await message.channel.send(response)
        # Make sure to include this to process commands in messages
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(GeneralEvents(bot))
