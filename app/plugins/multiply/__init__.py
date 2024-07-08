from app.commands import Command

class MultiplyCommand(Command):
    """Multiplication command"""
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            result = 1
            for number in numbers:
                result *= number
            arguments_str = ' '.join(map(str, args))
            self.history_manager.add_entry('multiply', arguments_str, result)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
