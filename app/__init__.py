import os
import logging
import logging.config
import pandas as pd
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.menu import MenuCommand
from app.plugins.history import (HistoryCommand, ClearHistoryCommand, 
                                 SaveHistoryCommand, LoadHistoryCommand, 
                                 DeleteHistoryCommand)

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

class App:
    def __init__(self):
        '''Config init function'''
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.history = pd.DataFrame(columns=['Operation', 'Arguments', 'Result'])
        self.command_handler = CommandHandler()
        self.register_commands()

    def configure_logging(self):
        logging.config.dictConfig(logging_config)
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def register_commands(self):
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("history", HistoryCommand(self.history))
        self.command_handler.register_command("clear_history", ClearHistoryCommand(self.history))
        self.command_handler.register_command("save_history", SaveHistoryCommand(self.history))
        self.command_handler.register_command("load_history", LoadHistoryCommand(self.history))
        self.command_handler.register_command("delete_history", DeleteHistoryCommand(self.history))

    def start(self):
        '''Start function to initiate'''
        logging.info("Application started. Press Enter without typing anything to exit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input == '':
                    logging.info("Application exit.")
                    break
                parts = user_input.split()
                command_name = parts[0]
                args = parts[1:]
                self.command_handler.execute_command(command_name, *args)
            except KeyError:
                logging.error(f"Unknown command: {user_input}")
            except Exception as e:
                logging.error(f"Error executing command: {e}")

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

if __name__ == "__main__":
    app = App()
    app.start()
