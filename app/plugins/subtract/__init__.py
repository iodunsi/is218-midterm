from app.commands import Command

class SubtractCommand(Command):
    """Subtraction command"""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            if len(numbers) != 2:
                raise ValueError("Subtraction requires exactly two numbers.")
            result = numbers[0] - numbers[1]
            arguments_str = ' '.join(map(str, args))
            self.history_manager.add_entry('subtract', arguments_str, result)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Invalid input. Please enter exactly two numbers.")
