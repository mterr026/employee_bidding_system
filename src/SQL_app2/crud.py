from sqlalchemy.orm import Session

from . import models, schemas

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




