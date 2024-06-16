from discord.ext import commands
import logging


class GeneralCommands(commands.Cog, name="General Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(bot):
    logging.getLogger(__name__).info("Setting up General Commands...")
    bot.add_cog(GeneralCommands(bot))
    logging.getLogger(__name__).info("General Commands setup complete.")
