from app.commands import Command

class SubtractCommand(Command):
    """Subtraction command"""
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            if len(numbers) != 2:
                print("Error: Subtract command requires exactly 2 arguments.")
                return
            result = numbers[0] - numbers[1]
            print(f"Result: {result}")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
