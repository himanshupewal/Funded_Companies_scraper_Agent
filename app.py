from fastapi import FastAPI
from graph import graph

app = FastAPI()


@app.post("/run")
def run():

    return graph.invoke({})