import whisper
from ideariver_core import BasePlugin  # Assuming you're using ideariver-core for plugin base

class TranscribeAudioPlugin(BasePlugin):
    """
    Plugin to transcribe audio using Whisper model.
    """

    def __init__(self):
        self.model = None

    def init(self, services):
        """
        Initialize the plugin with required services (like model loading).
        
        Args:
            services (dict): Dictionary of services (e.g., logging).
        """
        # Load the Whisper model once, so it doesn't need to be reloaded for each function call
        self.model = whisper.load_model("base")

    def run(self, input_data):
        """
        Transcribe the audio and return the transcript and timestamps.

        Args:
            input_data (dict): Dictionary containing 'audio_path' (path to audio file).

        Returns:
            dict: Transcript and timestamped segments.
        """
        audio_path = input_data.get('audio_path')
        if not audio_path:
            raise ValueError("The 'audio_path' field is required.")

        return self.transcribe_audio(audio_path)

    def transcribe_audio(self, audio_path):
        """Transcribes the audio and returns the transcript and timestamps."""
        try:
            result = self.model.transcribe(audio_path)
            transcript = result['text']
            segments = result['segments']  # Segments include timestamps
            return {
                "transcript": transcript,
                "segments": [
                    {
                        "start": segment["start"],
                        "end": segment["end"],
                        "text": segment["text"]
                    }
                    for segment in segments
                ]
            }
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return None
