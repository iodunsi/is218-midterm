"""This file will test application implementation"""
import logging
#import pytest
from app import App

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')

def test_app_menu_command(capfd):
    """Menu command"""
    app = App()
    app.command_handler.execute_command("menu")

    out, _ = capfd.readouterr()
    assert "Available commands:" in out
    assert "- add" in out
    assert "- subtract" in out
    assert "- multiply" in out
    assert "- divide" in out
    assert "- menu" in out

def test_app_add_command(capfd):
    """Add command"""
    app = App()
    app.command_handler.execute_command("add", 10, 20)

    out, _ = capfd.readouterr()
    assert "Result: 30.0" in out

def test_app_subtract_command(capfd):
    """Sub command"""
    app = App()
    app.command_handler.execute_command("subtract", 20, 10)

    out, _ = capfd.readouterr()
    assert "Result: 10.0" in out

def test_app_multiply_command(capfd):
    """Multiply command"""
    app = App()
    app.command_handler.execute_command("multiply", 3, 4)

    out, _ = capfd.readouterr()
    assert "Result: 12.0" in out

def test_app_divide_command(capfd):
    """Divide command"""
    app = App()
    app.command_handler.execute_command("divide", 8, 2)

    out, _ = capfd.readouterr()
    assert "Result: 4.0" in out

def test_app_divide_by_zero_command(capfd):
    """Handling div by zero exceptions"""
    app = App()
    app.command_handler.execute_command("divide", 8, 0)

    out, _ = capfd.readouterr()
    assert "Error: Division by zero" in out