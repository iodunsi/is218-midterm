from app.commands import Command

class SubCommand(Command):
    '''Subtraction command'''
    def execute(self, *args):
        a,b=map(float,args)
        result = a - b
        print(f"Result: {result}")