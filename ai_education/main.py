import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Define paths
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# Ensure necessary directories exist
os.makedirs(STATIC_DIR / "css", exist_ok=True)
os.makedirs(STATIC_DIR / "js", exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Debugging print
print(f"Static Directory Path: {STATIC_DIR}")  # Print to verify the static directory exists

app = FastAPI()

# Mount static folder correctly
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    """Home route to render the homepage overview of the platform."""
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/ai_learning")
async def ai_learning():
    """Route for AI learning, personalized learning features."""
    return {"message": "AI Learning Features"}

@app.get("/resources_hub")
async def resources_hub():
    """Route for resources hub, containing PDFs, videos, study materials."""
    return {"message": "Resources Hub"}

@app.get("/ethics_of_ai")
async def ethics_of_ai():
    """Route for Ethics of AI, emphasizing responsible AI learning."""
    return {"message": "Ethics of AI"}

@app.get("/about_us")
async def about_us():
    """Route for the 'About Us' section to display platform details."""
    return {"message": "About Us Information"}

@app.get("/contact_us")
async def contact_us():
    """Route for the 'Contact Us' section to provide support & inquiries."""
    return {"message": "Contact Us Information"}

@app.get("/chatbot")
async def chatbot(query: str):
    """Handles chatbot queries and stores logs."""
    response_text = "I am AI Chatbot! How can I help you?"
    
    return JSONResponse(content={"response": response_text})

# Optional logging to track content length and data
@app.middleware("http")
async def log_request(request: Request, call_next):
    response = await call_next(request)
    content_length = response.headers.get("content-length")
    if content_length:
        print(f"Response Content-Length: {content_length}")
    return response
