import pytest
import json
from write_youtube_description_nlp import write_youtube_description_nlp

@pytest.fixture
def sample_transcript():
    """
    Fixture to load sample transcript data from tmp/sample_transcript.json.
    """
    transcript_path = "tmp/sample_transcript.json"
    with open(transcript_path, 'r') as file:
        transcript_data = json.load(file)
        # print("Transcript Data:", transcript_data)
    return transcript_data

def test_write_youtube_description_nlp(sample_transcript):
    """
    Test the write_youtube_description_nlp function with the sample transcript from the file.
    """

    # Run the write_youtube_description_nlp function with the sample transcript
    description = write_youtube_description_nlp(sample_transcript)
    
    # Print the description to see the output
    print("Generated Description:", description)
    
    # Check that the description is not empty
    assert description, "No description was generated."

