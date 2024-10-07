import whisper

# Load the Whisper model once, so it doesn't need to be reloaded for each function call
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """Transcribes the audio and returns the transcript and timestamps."""
    try:
        result = model.transcribe(audio_path)
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
