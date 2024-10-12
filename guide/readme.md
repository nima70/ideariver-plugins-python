## Set Up the Project and Install Dependencies

Step 1: Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Linux: source venv/bin/activate
python ffmpeg.py    # to setup ffmpeg
```

## Step 2: Install the Dependencies

Run the following command to install the required dependencies:

```bash
pip install pytube whisper pytest
```

## This will install:

- pytube: For downloading YouTube videos.
- whisper: For transcribing audio.
- pytest: For running the unit tests.

# Step 3: Create a requirements.txt File

Once all the packages are installed, generate a requirements.txt file to track the dependencies:
If you've manually installed packages, such as python-dotenv, and want to update your requirements.txt to reflect these changes, run the following command:

```bash
pip freeze > requirements.txt
```

To run tests

```bash
pytest test_download.py

```

To ensure you see the transcription result printed in the terminal during the test, you can use the command pytest -s to run the test. This flag ensures that the print statements from the test are not suppressed.

```bash
pytest -s test_transcribe.py
```

This will create a requirements.txt file similar to the following:

```text
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
numpy==1.21.5
pytube==12.1.0
requests==2.27.1
tqdm==4.63.0
torch==1.11.0
typing-extensions==4.1.1
whisper==1.0
pytest==7.1.2
```

## Project Structure

Ensure your project is structured as follows:

```bash
transcription_service/
├── download.py
├── transcribe.py
├── test_download.py
├── test_transcribe.py
├── requirements.txt
├── Dockerfile  # Will create this later
└── README.md   # Optional: to document the project
```
