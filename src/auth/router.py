from fastapi import APIRouter, Request, Depends, Form
import auth.model
from fastapi.responses import HTMLResponse, RedirectResponse
from SQL_app2 import crud, models, schemas, database
from SQL_app2.database import SessionLocal, engine
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register")
def register(EIN: int = Form(...), fname: str = Form(...), lname: str = Form(...), startDate: str = Form(...), 
             role: str = Form(...), securityQuestion: str = Form(...), securityAnswer: str = Form(...),
               password: str = Form(...), db: Session = Depends(database.get_db)):
    newEmp = auth.model.Employee(EIN = EIN, fname = fname, lname = lname, startDate = startDate, role = role,
                            securityQuestion = securityQuestion, securityAnswer = securityAnswer, 
                            password = password)
    db.add(newEmp) 
    db.commit()
    message = "REGISTRATION SUCCESFUL"
    return RedirectResponse(url=f"/register?message={message}", status_code=303)