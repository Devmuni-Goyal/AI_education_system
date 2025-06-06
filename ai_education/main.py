import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import privacy_policy, terms

# Importing route modules for different sections of the platform
from ai_education.routes import ai_learning, resources_hub, ethics_ai, about_us, contact_us

# Define base directory and subdirectories for static files and templates
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# Ensure necessary directories exist for serving static files
os.makedirs(STATIC_DIR / "css", exist_ok=True)
os.makedirs(STATIC_DIR / "js", exist_ok=True)
os.makedirs(STATIC_DIR / "images", exist_ok=True)
os.makedirs(STATIC_DIR / "videos", exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Debugging print to verify directory existence
print(f"Static Directory Path: {STATIC_DIR}")

# Initialize FastAPI application
app = FastAPI()

# Register imported routes for different sections of the platform
app.include_router(ai_learning.router)
app.include_router(resources_hub.router)
app.include_router(ethics_ai.router)
app.include_router(about_us.router)
app.include_router(contact_us.router)

# Include Privacy Policy and Terms Routes
app.include_router(privacy_policy.router, prefix="/privacy-policy")
app.include_router(terms.router, prefix="/terms")

# Mount static folder to serve CSS, JS, images, and videos
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Set up Jinja2 templates for rendering HTML responses
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Home route to render the homepage
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# AI Learning Route
@app.get("/ai_learning", response_class=HTMLResponse)
async def ai_learning(request: Request):
   return templates.TemplateResponse("ai_learning.html", {"request": request})

# Resources Hub Route
@app.get("/resources_hub", response_class=HTMLResponse)
async def resources_hub(request: Request):
    return templates.TemplateResponse("resources_hub.html", {"request": request})

# Ethics of AI Route
@app.get("/ethics_of_ai", response_class=HTMLResponse)
async def ethics_of_ai(request: Request):
 return templates.TemplateResponse("ethics_ai.html", {"request": request})

# About Us Route (renders an HTML page)
@app.get("/about_us", response_class=HTMLResponse)
async def about_us_page(request: Request):
    return templates.TemplateResponse("about_us.html", {"request": request})

# Contact Us Route
@app.get("/contact_us", response_class=HTMLResponse)
async def contact_us(request: Request):
     return templates.TemplateResponse("contact_us.html", {"request": request})

# Privacy Policy Route
@app.get("/privacy-policy", response_class=HTMLResponse)
async def privacy_policy_page(request: Request):
    return templates.TemplateResponse("privacy_policy.html", {"request": request})

# Terms & Conditions Route
@app.get("/terms", response_class=HTMLResponse)
async def terms_page(request: Request):
    return templates.TemplateResponse("terms.html", {"request": request})

# Chatbot Route for handling chatbot queries
@app.get("/chatbot")
async def chatbot(query: str):
    response_text = "I am AI Chatbot! How can I help you?"
    return JSONResponse(content={"response": response_text})

# Middleware for logging response content length
@app.middleware("http")
async def log_request(request: Request, call_next):
    response = await call_next(request)
    content_length = response.headers.get("content-length")
    if content_length:
        print(f"Response Content-Length: {content_length}")
    return response
