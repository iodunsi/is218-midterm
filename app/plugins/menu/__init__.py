from app.commands import Command

class MenuCommand(Command):
    '''Menu command'''
    def execute(self, *args):
        print("Available commands:")
        print("- add")
        print("- subtract")
        print("- multiply")
        print("- divide")
        print("- menu")