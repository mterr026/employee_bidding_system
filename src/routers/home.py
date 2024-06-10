from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

@router.get("/home", tags=["users"])
async def name(request: Request):
    numberOne = 1
    numberTwo = 4
    sum = numberOne + numberTwo

    return templates.TemplateResponse("home.html", {"request": request, "title": "Home", "sum": sum})