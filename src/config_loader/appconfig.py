from dotenv import dotenv_values


class AppConfig:
    __config_files_path = ""
    discord_params = {}

    def __init__(self, config_files_path):
        self.__config_files_path = config_files_path
        self.load_env()

    def load_env(self):
        self.discord_params = dotenv_values()