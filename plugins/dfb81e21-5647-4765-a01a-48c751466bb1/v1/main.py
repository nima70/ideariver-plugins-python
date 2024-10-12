import os
import yt_dlp
from ideariver_core import BasePlugin

class DownloadAudioPlugin(BasePlugin):
    def __init__(self):
        self.services = None

    def init(self, services):
        """
        Initialize the plugin with required services.
        
        Args:
            services (dict): Dictionary of services (e.g., logging).
        """
        self.services = services

    def run(self, input_data):
        """
        Download the audio of a YouTube video.

        Args:
            input_data (dict): Dictionary with 'video_id' and optionally 'output_dir'.

        Returns:
            str: Absolute path to the downloaded audio file.
        """
        video_id = input_data.get('video_id')
        output_dir = input_data.get('output_dir', None)

        if not video_id:
            raise ValueError("The 'video_id' field is required.")

        try:
            return self.download_audio(video_id, output_dir)
        except Exception as e:
            raise ValueError(f"Error during audio download: {str(e)}")

    def download_audio(self, video_id, output_dir=None):
        """Downloads the audio of a YouTube video using yt-dlp, ensuring compatibility across Windows and Linux."""
        if output_dir is None:
            output_dir = os.path.join(os.path.expanduser("~"), "tmp") if os.name == 'nt' else "/tmp"

        os.makedirs(output_dir, exist_ok=True)

        url = f"https://www.youtube.com/watch?v={video_id}"
        output_path = os.path.join(output_dir, f"{video_id}.mp4")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            if 'entries' in info_dict:
                raise ValueError("Received a playlist or HTML page instead of the video.")
            
            ydl.download([url])

        absolute_path = os.path.abspath(output_path)
        return absolute_path
