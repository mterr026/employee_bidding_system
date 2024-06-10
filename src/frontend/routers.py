from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="src/frontend/templates")

@router.get("/home", tags=["home"])
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home", "sum": sum})

@router.get('/login', tags=["login"]) 
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"}) 