from fastapi import FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from frontend import frontend_router

app = FastAPI()

app.include_router(frontend_router)



 