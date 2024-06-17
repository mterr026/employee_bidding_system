from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from auth.router import router as auth_router
from frontend.routers import router as frontend_router
from SQL_app2 import crud, models, schemas, database
from SQL_app2.database import SessionLocal, engine
from sqlalchemy.orm import Session


# Create all tables in the database !!REMOVE BEFORE DEPLOYMENT!!
models.Base.metadata.create_all(bind=engine)

# Create an instance of FastAPI
app = FastAPI()

# Specify the directory for HTML templates
templates = Jinja2Templates(directory="frontend/templates")

# Include the routes from the frontend router
app.include_router(frontend_router)
app.include_router(auth_router)

# Endpoint to submit form data to the database
@app.post("/submit", response_model=schemas.UsersBase)
def submit_form(nameInput: str = Form(...), db: Session = Depends(database.get_db)):
    # Create a new user with the given name
    new_user = models.Users(name=nameInput)
    # Add the new user to the session
    db.add(new_user)
    # Commit the transaction to save the user in the database
    db.commit()
    # Redirect to the form page after submission
    return RedirectResponse(url="/form", status_code=303)

# Endpoint to display all users
@app.get("/display_users/", response_model=list[schemas.UsersBase], response_class=HTMLResponse)
def read_users(request: Request, db: Session = Depends(database.get_db)):
    # Query all users from the database
    get_users = db.query(models.Users).all()
    
    # Render the display_users.html template with the list of users
    return templates.TemplateResponse("display_users.html", {"request": request, "users": get_users})

# Endpoint to delete a specific user
@app.post("/delete_user", response_class=RedirectResponse)
def delete_user(user_name: str = Form(...), db: Session = Depends(database.get_db)):
    # Query the user with the given name from the database
    user = db.query(models.Users).filter(models.Users.name == user_name).first()
    # If the user exists, delete the user
    if user:
        db.delete(user)
        db.commit()
    # Redirect to the display_users page after deletion
    return RedirectResponse(url="/display_users", status_code=303)


