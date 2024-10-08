import pytest
from plugin import ConvertToMDXPlugin

@pytest.fixture
def transcript_text():
    """Sample transcript text to be converted to MDX."""
    return "This is a sample transcript text for MDX conversion."

@pytest.fixture
def plugin():
    """
    Fixture to initialize the ConvertToMDXPlugin instance.
    """
    plugin_instance = ConvertToMDXPlugin()
    plugin_instance.init(services={})  # Initialize with no services for now
    return plugin_instance

def test_convert_to_mdx(plugin, transcript_text):
    """
    Test the ConvertToMDXPlugin's functionality.
    """
    # Run the plugin with the transcript text
    input_data = {"transcript_text": transcript_text}
    output_file = plugin.run(input_data)
    
    # Check that the MDX file is generated
    assert output_file is not None, "No MDX file was generated."
    assert output_file == "transcript.mdx", "The generated file should be 'transcript.mdx'."

    # Check that the file has content
    with open(output_file, "r") as mdx_file:
        content = mdx_file.read()
    
    assert content, "The MDX file should contain generated content."
    print("Generated MDX Content:", content)
