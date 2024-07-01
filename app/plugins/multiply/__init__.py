from app.commands import Command

class MultCommand(Command):
    '''Multiplication command''' 
    def execute(self, *args):
        a, b = map(float, args)
        result = a * b
        print(f"Result: {result}")