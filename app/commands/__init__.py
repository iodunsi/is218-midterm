import importlib.util
import os

class CommandHandler:
    def __init__(self, plugin_dir='app/plugins'):
        self.commands = {}
        self.plugin_dir = plugin_dir
        self.load_plugins()

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module_path = os.path.join(self.plugin_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                        self.register_command(module_name, attribute())

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name, *args):
        command = self.commands.get(name)
        if command:
            command.execute(*args)
        else:
            print(f"No such command: {name}")

class Command:
    def execute(self, *args):
        raise NotImplementedError("Command subclasses must implement `execute` method")
    
__all__ = ['CommandHandler', 'Command', 'AddCommand'] 