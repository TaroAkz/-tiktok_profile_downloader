# TikTok Profile Downloader

A web-based application for downloading TikTok profile videos with a user-friendly interface. Built with FastAPI and yt-dlp.

## Features

- 🌐 **Web Interface**: Clean, intuitive web UI for easy interaction
- 📹 **Profile Downloads**: Download all videos from a TikTok profile
- 📊 **Profile Preview**: Fetch and preview profile information before downloading
- 🎯 **Batch Processing**: Download multiple videos at once
- 📂 **Organized Storage**: Videos saved in organized folder structure
- ⚡ **Fast Processing**: Leverages yt-dlp for efficient downloads

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **yt-dlp** (will be installed via requirements.txt)

## Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd tiktok_web_downloader
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv .tiktok_env
source .tiktok_env/bin/activate  # On Windows: .tiktok_env\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Application

1. **Activate the virtual environment (if not already activated):**

```bash
source .tiktok_env/bin/activate  # On Windows: .tiktok_env\Scripts\activate
```

2. **Run the FastAPI application:**

```bash
python -m uvicorn app.main:app --reload
```

3. **Open your browser and navigate to:**

```
http://localhost:8000
```

### How to Use

1. **Enter TikTok Profile URL**: Paste a TikTok profile URL in the input field (e.g., `https://www.tiktok.com/@username`)
2. **Fetch Profile**: Click "Fetch Profile" to preview the profile and see the number of posts
3. **Download**: Click "Download All" to start downloading all videos from the profile
4. **Check Downloads**: Downloaded videos are saved in the `downloads/` directory

## Project Structure

```
tiktok_web_downloader/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application and routes
│   ├── downloader.py           # Core downloading logic using yt-dlp
│   └── templates/
│       └── index.html          # Web UI template
├── downloads/                  # Folder where all downloaded videos are saved
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Configuration

- **Downloads Directory**: Videos are saved to the `downloads/` folder by default
- **Base Path**: Can be customized by modifying the `base_output_path` parameter in `app/main.py`

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI web server for running FastAPI
- **Jinja2**: Template engine for rendering HTML
- **yt-dlp**: Video downloader that supports TikTok
- **python-multipart**: For handling form data

See `requirements.txt` for a complete list of dependencies.

## API Endpoints

### GET `/`

Returns the main HTML interface

### POST `/fetch`

Fetches profile information and post count

- **Parameters**:
  - `profile_url` (form data): TikTok profile URL

### POST `/download`

Downloads all videos from a TikTok profile

- **Parameters**:
  - `profile_url` (form data): TikTok profile URL
- **Response**: JSON object with download status and file count

## Troubleshooting

### Issue: yt-dlp not found

**Solution**: Ensure yt-dlp is installed by running:

```bash
pip install yt-dlp --upgrade
```

### Issue: Videos not downloading

**Solution**: Verify the TikTok profile URL is correct and the profile is public

### Issue: Port 8000 already in use

**Solution**: Run on a different port:

```bash
python -m uvicorn app.main:app --reload --port 8001
```

## Limitations

- Only works with **public** TikTok profiles
- Downloads are limited by your internet connection speed
- Some videos may be unavailable due to regional restrictions

## License

This project is provided as-is for educational and personal use purposes.

## Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes.

## Disclaimer

This tool is for personal use only. Ensure you have the right to download content from the profiles you're accessing. Respect content creators' rights and TikTok's terms of service.
