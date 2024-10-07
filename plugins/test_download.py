import pytest
from plugins.download_audio_plugin.download import download_audio
import os

@pytest.fixture
def video_id():
    return "6nkF0WYy_Qo"  # Example YouTube video ID

def test_download_audio(video_id):
    """Test the download_audio function."""
    output_path = download_audio(video_id)
    
    # Normalize the path to ensure compatibility between Windows and Linux
    normalized_path = os.path.normpath(output_path)
    
    assert normalized_path is not None, "The download function should return a valid file path."
    assert os.path.exists(normalized_path), f"The file should exist after downloading. Path checked: {normalized_path}"
    
    # Cleanup
    os.remove(normalized_path)
