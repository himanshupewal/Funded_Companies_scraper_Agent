from fastapi import BackgroundTasks, FastAPI
from graph import graph

app = FastAPI()


def run_pipeline():
    graph.invoke({})


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Funding Agent API is live"
    }


@app.post("/run")
def run(background_tasks: BackgroundTasks):

    background_tasks.add_task(run_pipeline)

    return {
        "status": "started",
        "message": "Funding pipeline started. Check Railway logs for progress."
    }