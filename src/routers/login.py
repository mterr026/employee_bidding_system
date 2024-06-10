from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

@router.get('/login', tags=["login"]) 
async def name(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})  