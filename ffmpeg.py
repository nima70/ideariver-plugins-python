import os

ffmpeg_path = os.path.abspath("ffmpeg/bin")
os.environ["PATH"] += os.pathsep + ffmpeg_path
