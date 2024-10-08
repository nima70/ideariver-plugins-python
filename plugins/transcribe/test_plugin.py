import pytest
import os
from plugin import TranscribeAudioPlugin

@pytest.fixture
def audio_file():
    # Normalize the path to be compatible with Windows and Linux
    return os.path.normpath("tmp/sample_audio.mp4")

@pytest.fixture
def plugin():
    """
    Fixture to initialize the TranscribeAudioPlugin instance.
    """
    plugin_instance = TranscribeAudioPlugin()
    plugin_instance.init(services={})  # Initialize with no services for now
    return plugin_instance

def test_transcribe_audio(plugin, audio_file):
    """
    Test the TranscribeAudioPlugin's functionality with an audio file.
    """
    # Run the plugin with the audio file
    input_data = {"audio_path": audio_file}
    result = plugin.run(input_data)
    
    # Ensure the transcription result is valid
    assert result is not None, "Transcription result should not be None."
    assert "transcript" in result, "The result should contain a transcript."
    assert "segments" in result, "The result should contain segments with timestamps."
    
    # Print the result to see the transcript and segments
    print("\nTranscript:", result["transcript"])
    print("Segments:")
    for segment in result["segments"]:
        print(f"Start: {segment['start']}, End: {segment['end']}, Text: {segment['text']}")
