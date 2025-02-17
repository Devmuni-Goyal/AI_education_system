import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from ai_education.services import get_home_data  
from services import get_home_data  # Ensure this function is defined in services.py
from database import search_database, store_chatbot_log  # Ensure these exist in database.py

# Ensure the 'static' directory exists
os.makedirs("static", exist_ok=True)

app = FastAPI()

# Mounting static folder
app.mount("/static", StaticFiles(directory=os.path.abspath("static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_home():
    """Home route to render the homepage overview of the platform."""
    return get_home_data()

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
async def chatbot(query: str = Query(..., description="User's query")):
    """Handles chatbot queries and stores logs."""
    response_message = f"You asked: {query}. This is a placeholder response from the chatbot."
    
    # Storing chatbot log in the database
    store_chatbot_log(user_id=1, user_query=query, chatbot_response=response_message)
    
    return JSONResponse(content={"message": response_message})

@app.get("/search")
async def search(query: str):
    """Handles search queries and returns database results."""
    results = search_database(query)
    return JSONResponse(content={"query": query, "results": results})
