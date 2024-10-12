

import pytest
from .main import ConvertToMDXPlugin

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

    # Check that the MDX content is a string
    assert isinstance(mdx_content, str), "MDX content should be a string."
    
    # Loosely check for any form of headings, bullet points, or block elements
    contains_heading = "#" in mdx_content or "<h1>" in mdx_content or "##" in mdx_content
    contains_bullet_points = "-" in mdx_content or "*" in mdx_content
    contains_block_code = "```" in mdx_content or "<code>" in mdx_content

    assert contains_heading or contains_bullet_points or contains_block_code, "MDX content should contain headings, bullet points, or code blocks."

    # Print the generated MDX content for debugging
    print("Generated MDX Content:", mdx_content)

