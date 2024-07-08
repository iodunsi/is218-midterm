"""This file will be used to handle the history function of the calculator."""
import os
import pandas as pd

class HistoryManager:
    def __init__(self):
        """initialization"""
        self.history_df = pd.DataFrame(columns=['Operation', 'Arguments', 'Result'])

    def add_entry(self, operation, arguments, result):
        """function used to add history"""
        new_entry = pd.DataFrame([{'Operation': operation, 'Arguments': arguments, 'Result': str(result)}])
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)
        #print(f"Added operation: {new_entry}")
        #print(self.history_df)

    def clear_history(self):
        """function used to clear history"""
        self.history_df.drop(self.history_df.index, inplace=True)
        print("History cleared.")

    def save_history(self, file_path='history.csv'):
        """function used to save history"""
        self.history_df.to_csv(file_path, index=False)
        print(f"History saved to {file_path}.")

    def load_history(self, file_path='history.csv'):
        """function used to load history"""
        try:
            self.history_df = pd.read_csv(file_path, dtype=str)
            print(f"History loaded successfully with {len(self.history_df)} entries.")
        except FileNotFoundError:
            print(f"No history file found at {file_path}.")