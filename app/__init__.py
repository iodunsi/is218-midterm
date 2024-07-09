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
from app.history_manager import HistoryManager  # Import HistoryManager

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
        self.history_manager = HistoryManager()  
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
        self.command_handler.register_command("add", AddCommand(self.history_manager))  # Pass history_manager
        self.command_handler.register_command("divide", DivideCommand(self.history_manager))  # Pass history_manager
        self.command_handler.register_command("multiply", MultiplyCommand(self.history_manager))  # Pass history_manager
        self.command_handler.register_command("subtract", SubtractCommand(self.history_manager))  # Pass history_manager
        self.command_handler.register_command("menu", MenuCommand())

    def start(self):
        '''Start function to initiate'''
        logging.info("Application started. Press Enter without typing anything to exit. Type menu to see a list of commands.")
        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input == '':
                    logging.info("Application exit.")
                    break
                parts = user_input.split()
                command_name = parts[0]
                args = parts[1:]
                
                
                if command_name == 'load_history':
                    self.load_history(*args)
                elif command_name == 'save_history':
                    self.save_history(*args)
                elif command_name == 'clear_history':
                    self.clear_history()
                elif command_name == 'show_history':
                    self.show_history()
                else:
                    self.command_handler.execute_command(command_name, *args)
            except KeyError:
                logging.error(f"Unknown command: {user_input}")
            except Exception as e:
                logging.error(f"Error executing command: {e}")

    def load_history(self, file_path='history.csv'):
        '''Load history from a file'''
        self.history_manager.load_history(file_path)

    def save_history(self, file_path='history.csv'):
        '''Save history to a file'''
        self.history_manager.save_history(file_path)

    def clear_history(self):
        '''Clear the history'''
        self.history_manager.clear_history()

    def show_history(self):
        '''Display the history'''
        if self.history_manager.history_df.empty:
            print("No history available.")
        else:
            print(self.history_manager.history_df)

                
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

if __name__ == "__main__":
    app = App()
    app.start()
