from config_loader.appconfig import AppConfig
import os

# Assuming your .env and other config files are in the same directory as bot.py
bot_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Initialize AppConfig and load the environment variables globally
config = AppConfig(bot_dir)
