from app.commands import Command


class AddCommand(Command):
    """Addition command"""

    def __init__(self, history_manager):
        super().__init__()
        self.history_manager = history_manager
    
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            result = sum(numbers)
            arguments_str = ' '.join(map(str, args))
            self.history_manager.add_entry('add', arguments_str, result)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")