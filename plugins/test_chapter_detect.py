import pytest
import json
from detect_chapters_nlp import detect_chapters_nlp

@pytest.fixture
def sample_transcript():
    """Fixture to load sample transcript data from tmp/sample_transcript.json."""
    transcript_path = "tmp/sample_transcript.json"
    with open(transcript_path, 'r') as file:
        transcript_data = json.load(file)
        print("Transcript Data:", transcript_data)
    return transcript_data

def test_detect_chapters_nlp(sample_transcript):
    """
    Test the detect_chapters_nlp function with the sample transcript from the file.
    """

    # Run the detect_chapters_nlp function with the sample transcript
    chapters = detect_chapters_nlp(sample_transcript)
    # Print the chapters to see the output
    print("Detected Chapters:", chapters)
    # Check that the detected chapters are not empty
    assert chapters, "Chapter detection did not return any chapters."

