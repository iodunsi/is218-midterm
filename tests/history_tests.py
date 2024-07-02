"""
This file will test history command implementation.
"""
import os
import pandas as pd
import pytest
from app.plugins.history import LoadHistoryCommand

@pytest.fixture
def history_fixture():
    """Fixture for creating a sample history DataFrame."""
    data = {
        'Operation': ['add', 'subtract'],
        'Arguments': ['10 20', '30 20'],
        'Result': ['30', '10']
    }
    return pd.DataFrame(data)

def test_load_history_command(history_fixture):
    """Test load history command."""
    # Save history to test_history.csv
    history_fixture.to_csv('test_history.csv', index=False)

    # Create an empty history DataFrame
    empty_history = pd.DataFrame(columns=['Operation', 'Arguments', 'Result'])

    # Execute the load history command
    command = LoadHistoryCommand(empty_history)
    command.execute('test_history.csv')

    # Check the loaded history matches expectations
    assert not empty_history.empty
    assert list(empty_history['Operation']) == ['add', 'subtract']
    assert list(empty_history['Arguments']) == ['10 20', '30 20']
    assert list(empty_history['Result'].astype(str)) == ['30', '10']

    # Clean up
    os.remove('test_history.csv')
