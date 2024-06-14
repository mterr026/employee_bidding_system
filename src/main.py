# src/main.py
from fastapi import FastAPI, APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from frontend.routers import router as frontend_router
from SQL_app import models
from SQL_app.config import DATABASE

app = FastAPI()

templates = Jinja2Templates(directory="frontend/templates")

app.include_router(frontend_router)

#Check if database is connected, if not create connection
def get_db():
    if DATABASE.is_closed():
        DATABASE.connect()
    try:
        yield
    finally:
        if not DATABASE.is_closed():
            DATABASE.close()

#sends information from form to the database
@app.post("/submit", dependencies=[Depends(get_db)])
def submit_form(name: str = Form(...)):
    user_object = models.Users.create(name=name)
    return RedirectResponse(url="/form", status_code=303)

#pulls all users from the database and displays in users.html page
@app.get("/display_users", response_class=HTMLResponse)
def display_users(request: Request):
    users = list(models.Users.select())
    return templates.TemplateResponse("display_users.html", {"request": request, "users": users})

@app.post("/delete_user", dependencies=[Depends(get_db)])
def delete_user(user_id: int = Form(...)):
    user = models.Users.get(models.Users.id == user_id)
    user.delete_instance()
    return RedirectResponse(url="/display_users", status_code=303)


 