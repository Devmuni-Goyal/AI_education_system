from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="ai_education/templates")

@router.get("/resources-hub")
async def resources_hub_page(request: Request):
    return templates.TemplateResponse("resources_hub.html", {"request": request})
