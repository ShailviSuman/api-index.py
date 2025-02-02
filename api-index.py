from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the marks data from a JSON file
def load_marks_data():
    with open("q-vercel-python.json", "r") as file:
        return json.load(file)

marks_data = load_marks_data()

@app.get("/api")
def get_marks(names: list[str] = Query(...)):
    marks = [marks_data.get(name, 0) for name in names]
    return {"marks": marks}
ame in names]
    return {"marks": marks}
