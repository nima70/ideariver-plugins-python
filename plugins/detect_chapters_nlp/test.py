import pytest
import json
from .main import ChapterDetectionPlugin

@pytest.fixture
def sample_transcript():
    """Fixture to load sample transcript data from tmp/sample_transcript.json."""
    transcript_path = "assets/sample_transcript.json"
    with open(transcript_path, 'r') as file:
        transcript_data = json.load(file)
        print("Transcript Data:", transcript_data)
    return transcript_data

@pytest.fixture
def plugin():
    """
    Fixture to initialize the ChapterDetectionPlugin instance.
    """
    plugin_instance = ChapterDetectionPlugin()
    plugin_instance.init(services={})  # Initialize without services for this test
    return plugin_instance

def test_detect_chapters_nlp(plugin, sample_transcript):
    """
    Test the ChapterDetectionPlugin's ability to detect chapters using sample transcript.
    """

    # Run the ChapterDetectionPlugin with the sample transcript
    chapters = plugin.run(sample_transcript)

    # Print the detected chapters to inspect the output
    print("Detected Chapters:", chapters)

    # Check that the detected chapters are not empty
    assert chapters, "Chapter detection did not return any chapters."
