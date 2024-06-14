from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")

#Sets endpoint to home page and passes a variable to the html
@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home", "sum": sum})

#sets endpoint to form page and passes a variable to the html
@router.get('/form') 
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "title": "Form"}) 