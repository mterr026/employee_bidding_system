from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

templates = Jinja2Templates(directory="templates")



@app.get('/')
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home"})

@app.get('/login') 
async def name(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})  


 