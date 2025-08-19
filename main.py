from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from typing import Dict, List
from urllib.parse import quote

app = FastAPI(
    title="Empire Agency",
    description="Агентство Empire Анны Чернавских - PR и медиасопровождение",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates setup
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Main page route"""
    return FileResponse("static/app.html")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Empire Agency is running! 🚀"}

@app.get("/whoami")
async def whoami(request: Request):
    """Debug endpoint to verify external access and see your IP from the server perspective"""
    client_ip = request.client.host if request.client else None
    return {
        "client_ip": client_ip,
        "user_agent": request.headers.get("user-agent"),
    }

@app.get("/client", response_class=HTMLResponse)
async def client_page(request: Request):
    """Alternate entry page so you can quickly open via http://<server-ip>:<port>/client"""
    return FileResponse("static/app.html")

@app.get("/api/info")
async def api_info():
    """API information endpoint"""
    return {
        "name": "Empire Agency",
        "description": "PR и медиасопровождение артистов и инфлюенсеров",
        "contact": {
            "phone": "+7 (906) 770-07-03",
            "email": "pr@empireagency.ru",
            "whatsapp": "https://wa.me/79067700703",
            "telegram": "@agencyempire"
        }
    }


def _list_case_images() -> Dict[str, List[str]]:
    """Scan static/cases/* folders and return web paths for images per folder.

    Keys are folder names. Values are URL paths beginning with /static/...
    Only common image extensions are included. Files are sorted by name.
    """
    base_dir = os.path.join("static", "cases")
    allowed_ext = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".JPG", ".JPEG", ".PNG", ".WEBP", ".GIF"}
    result: Dict[str, List[str]] = {}
    if not os.path.isdir(base_dir):
        return result
    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue
        images: List[str] = []
        try:
            for fname in sorted(os.listdir(folder_path)):
                # skip hidden/system files like ._*, .DS_Store, Thumbs.db
                if fname.startswith('.'):
                    continue
                low = fname.lower()
                if low in {'.ds_store', 'thumbs.db'}:
                    continue
                fpath = os.path.join(folder_path, fname)
                if not os.path.isfile(fpath):
                    continue
                _, ext = os.path.splitext(fname)
                if ext in allowed_ext:
                    web_path = f"/static/cases/{quote(folder)}/{quote(fname)}"
                    images.append(web_path)
        except Exception:
            # ignore folder read errors
            pass
        result[folder] = images
    return result


@app.get("/api/cases")
async def api_cases():
    """Return available case images grouped by folder.

    Example output:
    { "cases": { "indilite": ["/static/cases/indilite/.."], "venom": [ ... ] } }
    """
    return {"cases": _list_case_images()}

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    # Allow overriding port via PORT or APP_PORT env var
    port = int(os.getenv("PORT", os.getenv("APP_PORT", "8000")))
    # Enable auto-reload by default for local runs; set RELOAD=false on server
    reload = os.getenv("RELOAD", "true").lower() == "true"
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )
