from app.app import app
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse


app.mount("/public", StaticFiles(directory="public", html=True), name="public")


@app.get("/")
def read_index():
    return FileResponse(f"public/index.html")


@app.get("/js/{f}")
def read_js(f):
    return FileResponse(f"public/js/{f}")


@app.get("/css/{f}")
def read_css(f):
    return FileResponse(f"public/css/{f}")


@app.get("/fonts/{f}")
def read_fonts(f):
    return FileResponse(f"public/fonts/{f}")


@app.get("/favicon.ico")
def read_favico():
    return FileResponse("public/favicon.ico")
