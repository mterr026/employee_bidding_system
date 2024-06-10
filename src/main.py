from fastapi import FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from frontend.routers import frontend_router

app = FastAPI()

app.include_router(frontend_router)


@app.get('/home')
async def root(request: Request):
    numberOne = 1
    numberTwo = 4
    sum = numberOne + numberTwo
    return {"title": "Home", "sum": sum}


 