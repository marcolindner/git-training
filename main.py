from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"

@app.get("/todos")
def get_todos():
    return "Get Todo"
