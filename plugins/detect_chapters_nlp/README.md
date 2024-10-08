# Chapter Detection Plugin

The **Chapter Detection Plugin** uses OpenAI's LLM to analyze video transcripts and generate meaningful chapters with timestamps. This plugin helps segment videos into chapters, making it easier for users to navigate content.

## Key Features:

- 🧠 **AI-Powered Chapter Detection**: Automatically detects chapters based on transcript content.
- ⏱️ **Timestamp Generation**: Creates timestamps for easy navigation in YouTube format.
- 📁 **Flexible Input**: Accepts transcript segments in JSON format, making it easy to integrate.

## How It Works:

1. Provide the video transcript in a JSON format with time-stamped segments.
2. The plugin analyzes the content and outputs a list of chapters with timestamps.

### Example Input:

```json
{
  "segments": [
    { "start": 0.0, "end": 5.0, "text": "Hello and welcome to the video." },
    {
      "start": 5.0,
      "end": 10.0,
      "text": "We are going to discuss some important topics."
    },
    { "start": 10.0, "end": 20.0, "text": "Let's get into the main topic now." }
  ]
}
```
