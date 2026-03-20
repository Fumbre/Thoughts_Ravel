import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from representation_engin.main import generate_graph

load_dotenv()

app = FastAPI()

# Get the string from .env and split it by the comma into a list
origins_str = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173")
origins = origins_str.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/graph")
def get_graph():
    return generate_graph()


if __name__ == "__main__" :
    uvicorn.run("app:main", host="0.0.0.0", port=3000, reload=True)