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
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
