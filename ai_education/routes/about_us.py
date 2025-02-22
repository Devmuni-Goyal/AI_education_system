from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="ai_education/templates")

@router.get("/about-us")
async def about_us_page(request: Request):
    return templates.TemplateResponse("about_us.html", {"request": request})
