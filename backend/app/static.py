import os
from typing import Optional
from app.app import app
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates


base_path = os.path.dirname(os.path.realpath(__file__))

app.mount(
    "/public",
    StaticFiles(directory=f"{base_path}/public", html=True),
    name="public",
)
templates = Jinja2Templates(directory="public")


@app.get("/{full_path:path}")
def static(request: Request, full_path: str):
    return templates.TemplateResponse("index.html", {"request": request})
