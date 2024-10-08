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
    mdx_content = plugin.run(input_data)
    
    # Check that the MDX content is generated
    assert mdx_content is not None, "No MDX content was generated."
    
    # Check that the MDX content is a string and has proper formatting
    assert isinstance(mdx_content, str), "MDX content should be a string."
    assert "<h1>" in mdx_content or "##" in mdx_content, "MDX content should contain headings."
    
    # Print the generated MDX content for debugging
    print("Generated MDX Content:", mdx_content)
