import pytest
import json
from plugin import YouTubeDescriptionPlugin

@pytest.fixture
def sample_transcript():
    """
    Fixture to load sample transcript data from tmp/sample_transcript.json.
    """
    transcript_path = "tmp/sample_transcript.json"
    with open(transcript_path, 'r') as file:
        transcript_data = json.load(file)
    return transcript_data

@pytest.fixture
def plugin():
    """
    Fixture to initialize the YouTubeDescriptionPlugin instance.
    """
    plugin_instance = YouTubeDescriptionPlugin()
    plugin_instance.init(services={})  # Initialize with no services for now
    return plugin_instance

def test_write_youtube_description(plugin, sample_transcript):
    """
    Test the YouTubeDescriptionPlugin's functionality.
    """
    # Run the plugin with the sample transcript
    description = plugin.run(sample_transcript)
    
    # Print the generated description to see the output
    print("Generated Description:", description)
    
    # Check that the description is not empty
    assert description, "No description was generated."
