from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Sample data: Marks of 100 imaginary students
marks_data = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40,
    "Eve": 50,
    # Add more names and marks as needed
}

@app.get("/api")
def get_marks(names: list[str] = Query(...)):
    marks = [marks_data.get(name, 0) for name in names]
    return {"marks": marks}
