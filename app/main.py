# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.downloader import fetch_profile_posts, download_profile

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/fetch", response_class=HTMLResponse)
def fetch_posts(request: Request, profile_url: str = Form(...)):
    data = fetch_profile_posts(profile_url)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "profile_url": profile_url,
            "username": data["username"],
            "post_count": len(data["posts"])
        }
    )


@app.post("/download")
def download(profile_url: str = Form(...)):
    try:
        result = download_profile(profile_url, base_output_path="downloads")
        return {
            "status": "success",
            "message": f"Download completed! {result['total_files']} files saved to {result['base_path']}",
            "total_files": result["total_files"],
            "base_path": result["base_path"]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Download failed: {str(e)}"
        }