# test_sum_plugin.py
import pytest
from .main import SumPlugin

@pytest.fixture
def input_data():
    return {"a": 1, "b": 2}

@pytest.fixture
def plugin():
    """
    Fixture to initialize the SumPlugin instance.
    """
    plugin_instance = SumPlugin()
    plugin_instance.init(services={})  # No services required for this example
    return plugin_instance

def test_sum_plugin(plugin, input_data):
    """
    Test the SumPlugin's sum calculation functionality.
    """
    output = plugin.run(input_data)
    assert output == {"sum": 3}, f"Expected {{'sum': 3}}, but got {output}"
