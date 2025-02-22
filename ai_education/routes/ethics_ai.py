from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="ai_education/templates")

@router.get("/ethics-ai")
async def ethics_ai_page(request: Request):
    return templates.TemplateResponse("ethics_ai.html", {"request": request})
