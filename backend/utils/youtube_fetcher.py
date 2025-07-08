import yt_dlp
import os
import json

def load_metadata(metadata_path="downloads/metadata.json"):
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            return json.load(f)
    return {}

def save_metadata(metadata, metadata_path="downloads/metadata.json"):
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

def download_audio_from_youtube(search_query: str, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    metadata_path = os.path.join(output_dir, "metadata.json")
    metadata = load_metadata(metadata_path)

    # Extract video info only (don't download yet)
    ydl_opts_info = {
        "quiet": True,
        "skip_download": True,
        "default_search": "ytsearch",
    }

    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info = ydl.extract_info(search_query, download=False)
        if "entries" in info:
            info = info["entries"][0]
        video_id = info["id"]

        # Check if already downloaded
        if video_id in metadata:
            print(f"Video already downloaded: {metadata[video_id]}")
            return metadata[video_id]

        # Proceed with download
        output_template = os.path.join(output_dir, "%(title)s.%(ext)s")
        ydl_opts_download = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "default_search": "ytsearch",
            "outtmpl": output_template,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts_download) as ydl_download:
            info = ydl_download.extract_info(search_query, download=True)
            if "entries" in info:
                info = info["entries"][0]
            title = info["title"]
            file_path = os.path.join(output_dir, f"{title}.mp3")

            # Update metadata
            metadata[video_id] = file_path
            save_metadata(metadata, metadata_path)

            return file_path
