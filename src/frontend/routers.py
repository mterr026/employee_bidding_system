from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")

#Sets endpoint to home page and passes a variable to the html
@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home"})

@router.get("/register")
def home(request: Request, message: str = None):
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register", "request": request, "message": message})

#sets endpoint to form page and passes a variable to the html
@router.get('/form') 
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "title": "register"}) 