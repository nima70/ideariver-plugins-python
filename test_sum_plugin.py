import pytest
from plugin_loader import PluginLoader

@pytest.fixture
def input_data():
    """
    Fixture to provide sample input data for the plugin.
    """
    return {"a": 1, "b": 2}

@pytest.fixture
def plugin_loader():
    """
    Fixture to initialize the PluginLoader and load the SumPlugin.
    """
    # Create an instance of the PluginLoader and specify the folder where plugins are stored
    loader = PluginLoader(plugins_folder="plugins")

    # Add the SumPlugin by loading its metadata file
    loader.add_plugin("plugins/sum/metadata.json")

    # Initialize the plugin (if needed)
    loader.init_plugin("sum_plugin", {})

    return loader

def test_sum_plugin_via_loader(plugin_loader, input_data):
    """
    Test the SumPlugin through the PluginLoader.
    """
    # Run the plugin via the loader
    output = plugin_loader.run_plugin("sum_plugin", input_data)

    # Check that the output matches the expected result
    assert output == {"sum": 3}, f"Expected {{'sum': 3}}, but got {output}"
