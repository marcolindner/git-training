from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"

@app.get("/todos")
def get_todos():
    return "Get Todo"

@app.put("/todo")
def put_todos():
    return "Put Todo"