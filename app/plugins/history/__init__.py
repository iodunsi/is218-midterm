import os
import pandas as pd
from app.commands import Command

class HistoryCommand(Command):
    def __init__(self, history_df):
        self.history_df = history_df

    def execute(self):
        print(self.history_df)

class ClearHistoryCommand(Command):
    def __init__(self, history_df):
        self.history_df = history_df

    def execute(self):
        self.history_df.drop(self.history_df.index, inplace=True)
        print("History cleared.")

class SaveHistoryCommand(Command):
    def __init__(self, history_df):
        self.history_df = history_df

    def execute(self, file_path='history.csv'):
        self.history_df.to_csv(file_path, index=False)
        print(f"History saved to {file_path}.")

class LoadHistoryCommand(Command):
    def __init__(self, history_df):
        self.history_df = history_df

    def execute(self, file_path='history.csv'):
        if os.path.exists(file_path):
            loaded_df = pd.read_csv(file_path, dtype=str)  # Ensure all columns are read as strings
            self.load_history(loaded_df)
        else:
            print(f"No history file found at {file_path}.")

    def load_history(self, loaded_df):
        # Ensure column names match exactly
        loaded_df.columns = ['Operation', 'Arguments', 'Result']

        # Check and adjust data types if necessary
        loaded_df['Result'] = loaded_df['Result'].astype(str)  # Ensure Result is string type

        # Reset index if needed
        loaded_df.reset_index(drop=True, inplace=True)

        # Assign loaded data to history_df
        self.history_df[:] = loaded_df
        print(f"History loaded successfully with {len(loaded_df)} entries.")


class DeleteHistoryCommand(Command):
    def __init__(self, history_df):
        self.history_df = history_df

    def execute(self, file_path='history.csv'):
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"History file {file_path} deleted.")
        else:
            print(f"No history file found at {file_path}.")
