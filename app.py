
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/api")
def run():
    
    return result if 'result' in locals() else data

@app.get("/")
def ui():
    return HTMLResponse(open("index.html").read())
