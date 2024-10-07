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


# import pytest
# import json
# from detect_chapters_nlp import detect_chapters_nlp

# @pytest.fixture
# def sample_transcript():
#     """Fixture to load sample transcript data."""
#     return {
#         "segments": [
#             {"start": 0.0, "end": 6.3, "text": "Hello guys, today I'm trying to explain..."},
#             {"start": 6.3, "end": 10.0, "text": "Application in a CI CD pipeline..."},
#             {"start": 10.0, "end": 20.0, "text": "Now, we are going to discuss the main topic..."}
#         ]
#     }

# def test_detect_chapters_nlp(monkeypatch, sample_transcript):
#     """
#     Test the detect_chapters_nlp function.
#     Mock the LangChain LLM call to return a simulated chapter structure.
#     """

#     # Define a simulated LangChain response
#     simulated_response = "00:00 Introduction\n10:00 Main Topic\n20:00 Conclusion"

#     # Monkeypatch the LangChain invoke method
#     def mock_chain_invoke(input_data):
#         return simulated_response

#     # Monkeypatch the `invoke` method on the chain
#     monkeypatch.setattr('detect_chapters_nlp.chain.invoke', mock_chain_invoke)

#     # Run the detect_chapters_nlp function with the sample transcript
#     chapters = detect_chapters_nlp(sample_transcript)

#     # Check that the detected chapters match the expected simulated response
#     expected_chapters = "00:00 Introduction\n10:00 Main Topic\n20:00 Conclusion"
#     assert chapters == expected_chapters, "Chapter detection did not return the expected result."
