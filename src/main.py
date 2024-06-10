from fastapi import FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from src.routers import home_router, login_router

app = FastAPI()

app.include_router(home_router)
app.include_router(login_router)




 