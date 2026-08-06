import os
from dotenv import load_dotenv

from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from graph import graph

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def run_pipeline():
    graph.invoke({})


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "sheet_url": os.getenv("GOOGLE_SHEET_URL"),
        },
    )


@app.post("/run")
async def run(background_tasks: BackgroundTasks):

    background_tasks.add_task(run_pipeline)

    return {
        "status": "started",
        "message": "Funding pipeline started.",
    }