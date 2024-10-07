import os
import yt_dlp

def download_audio(video_id, output_dir=None):
    """Downloads the audio of a YouTube video using yt-dlp, ensuring compatibility across Windows and Linux."""

    try:
        # If no output directory is provided, set a default one based on the OS
        if output_dir is None:
            output_dir = os.path.join(os.path.expanduser("~"), "tmp") if os.name == 'nt' else "/tmp"

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        url = f"https://www.youtube.com/watch?v={video_id}"
        output_path = os.path.join(output_dir, f"{video_id}.mp4")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'noplaylist': True,
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            if 'entries' in info_dict:
                raise ValueError("Received a playlist or HTML page instead of the video.")
            
            ydl.download([url])

        # Convert relative path to absolute path to ensure compatibility between systems
        absolute_path = os.path.abspath(output_path)
        return absolute_path

    except Exception as e:
        print(f"Error downloading video: {e}")
        return None
