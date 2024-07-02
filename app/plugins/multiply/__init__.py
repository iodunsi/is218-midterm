from app.commands import Command

class MultiplyCommand(Command):
    """Multiplication command"""
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            result = 1
            for number in numbers:
                result *= number
            print(f"Result: {result}")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
