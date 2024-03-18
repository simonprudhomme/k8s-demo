# Simple fastapi server, with a single endpoint, that returns Hello World
# Run with, on port 80, with the following command: 
# uvicorn server:app --host 0.0.0.0 --port 80

# imports
from fastapi import FastAPI
import uvicorn
import os

# create an instance of the FastAPI class

app = FastAPI()

# define a route
@app.get("/")
def read_root():
    return {"Hello": f"World, from {os.environ.get('HOSTNAME', 'UNKNOWN')}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)