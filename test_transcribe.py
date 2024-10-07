import pytest
from transcribe import transcribe_audio
import os

@pytest.fixture
def audio_file():
    # Normalize the path to be compatible with Windows and Linux
    return os.path.normpath("tmp/sample_audio.mp4")

def test_transcribe_audio(audio_file):
    """Test the transcribe_audio function and print the result."""
    result = transcribe_audio(audio_file)
    
    assert result is not None, "Transcription result should not be None."
    assert "transcript" in result, "The result should contain a transcript."
    assert "segments" in result, "The result should contain segments with timestamps."
    
    # Print the result to see the transcript and segments
    print("\nTranscript:", result["transcript"])
    print("Segments:")
    for segment in result["segments"]:
        print(f"Start: {segment['start']}, End: {segment['end']}, Text: {segment['text']}")
