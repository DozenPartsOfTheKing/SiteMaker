from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os

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

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    # Allow overriding port via PORT or APP_PORT env var
    port = int(os.getenv("PORT", os.getenv("APP_PORT", "3001")))
    # Enable auto-reload by default for local runs; set RELOAD=false on server
    reload = os.getenv("RELOAD", "true").lower() == "true"
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )
