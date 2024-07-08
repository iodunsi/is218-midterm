import pandas as pd
from app.commands import Command

class DivideCommand(Command):
    """Division command"""

    def __init__(self, history_manager):
        super().__init__()
        self.history_manager = history_manager
    
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            if len(numbers) != 2 or numbers[1] == 0:
                raise ValueError("Division requires exactly two numbers and divisor must not be zero.")
            result = numbers[0] / numbers[1]
            arguments_str = ' '.join(map(str, args))
            self.history_manager.add_entry('divide', arguments_str, result)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Invalid input. Please enter two numbers and the divisor must not be zero.")