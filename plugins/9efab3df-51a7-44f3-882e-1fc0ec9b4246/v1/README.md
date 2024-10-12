# Transcribe Audio Plugin

The **Transcribe Audio Plugin** allows you to easily transcribe audio files using the Whisper model. It returns the transcription along with timestamps for each segment, making it ideal for projects involving videos, podcasts, or audio analysis.

## Key Features:

- 🎤 **Audio Transcription**: Transcribes any audio file into text.
- ⏱️ **Timestamps Included**: Provides start and end times for each segment of the audio.
- 📁 **Flexible Input**: Accepts any audio file path, making it easy to integrate.

## How It Works:

1. Provide the path to the audio file you want to transcribe.
2. The plugin uses Whisper to process the audio and returns both the transcript and the timestamped segments.

### Example Input:

```json
{
  "audio_path": "path/to/audio/file.mp3"
}
```
