from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="ai_education/templates")

@router.get("/ai-learning")
async def ai_learning_page(request: Request):
    return templates.TemplateResponse("ai_learning.html", {"request": request})
