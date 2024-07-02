from app.commands import Command

class AddCommand(Command):
    """Addition command"""
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            result = sum(numbers)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
