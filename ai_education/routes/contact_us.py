from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="ai_education/templates")

@router.get("/contact-us")
async def contact_us_page(request: Request):
    return templates.TemplateResponse("contact_us.html", {"request": request})

@router.post("/contact-us")
async def submit_contact_form(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    return {"message": "Form submitted successfully", "name": name, "email": email, "content": message}
