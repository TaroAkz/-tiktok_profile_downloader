import subprocess
import json
import os
from typing import Dict, List
from pathlib import Path


def fetch_profile_posts(profile_url: str) -> Dict[str, List[str]]:
    """
    Fetch TikTok profile posts without downloading videos.
    Returns:
        {
            "username": str,
            "posts": [post_id, ...]
        }
    """

    command = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--ignore-errors",
        profile_url
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        posts = []
        username = None

        for line in result.stdout.splitlines():
            if not line.strip():
                continue

            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue

            if not username:
                username = data.get("uploader") or data.get("uploader_id")

            post_id = data.get("id")
            if post_id:
                posts.append(post_id)

        return {
            "username": username,
            "posts": posts
        }

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to fetch profile:\n{e.stderr}")


# -------------------------------------------------------------

def download_profile(profile_url: str, base_output_path: str) -> Dict[str, any]:
    """
    Download ALL videos from a TikTok profile.
    Saves video + metadata.
    Returns info about downloaded files.
    """

    # Create output directory if it doesn't exist
    os.makedirs(base_output_path, exist_ok=True)

    output_template = os.path.join(
        base_output_path,
        "%(uploader)s",
        "%(id)s.%(ext)s"
    )

    command = [
        "yt-dlp",
        profile_url,
        "-o", output_template,
        "--write-info-json",
        "--ignore-errors",
        "--no-overwrites",
        "--yes-playlist",
        "--retries", "3",
        "--fragment-retries", "3"
    ]

    try:
        subprocess.run(command, check=True)
        
        # Count downloaded files
        total_files = 0
        for root, dirs, files in os.walk(base_output_path):
            total_files += len(files)
        
        return {
            "success": True,
            "base_path": base_output_path,
            "total_files": total_files
        }

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Profile download failed:\n{e}")


# -------------------------------------------------------------

def download_single_post(post_url: str, base_output_path: str) -> Dict[str, any]:
    """
    Download ONE TikTok video only.
    Useful for DB-controlled downloading.
    Returns info about downloaded files.
    """

    # Create output directory if it doesn't exist
    os.makedirs(base_output_path, exist_ok=True)

    output_template = os.path.join(
        base_output_path,
        "%(uploader)s",
        "%(id)s.%(ext)s"
    )

    command = [
        "yt-dlp",
        post_url,
        "-o", output_template,
        "--write-info-json",
        "--no-playlist",
        "--retries", "3",
        "--fragment-retries", "3"
    ]

    try:
        subprocess.run(command, check=True)
        
        # Count downloaded files
        total_files = 0
        for root, dirs, files in os.walk(base_output_path):
            total_files += len(files)
        
        return {
            "success": True,
            "base_path": base_output_path,
            "total_files": total_files
        }

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Post download failed:\n{e}")