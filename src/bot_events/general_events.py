import discord
from discord.ext import commands
import logging


class GeneralEvents(commands.Cog, name="General Events"):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config  # Store the passed config
        self.logger = logging.getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self):
        guild_name = self.config.discord_params['DISCORD_GUILD']
        guild = discord.utils.get(self.bot.guilds, name=guild_name)
        if guild:
            self.logger.info(
                f'{self.bot.user.name} has connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
            members = '\n - '.join([member.name for member in guild.members])
            self.logger.info(f'Guild members:\n - {members}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "help":
            await message.channel.send("Testing 1 2 3")


def setup(bot, config):  # Adjust the setup function to receive config
    logging.getLogger(__name__).info("Setting up General Events...")
    bot.add_cog(GeneralEvents(bot, config))
    logging.getLogger(__name__).info("General Events setup complete.")
