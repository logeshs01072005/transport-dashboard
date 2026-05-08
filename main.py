from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# Fix path for Render
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Store data in memory
stored_data = []

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# Home route
@app.get("/")
def home():
    return FileResponse(os.path.join(BASE_DIR, "static", "transport-dashboard.html"))

# POST → Upload file
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    global stored_data
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file, on_bad_lines='skip')

        elif file.filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)

        else:
            return {"error": "Only CSV or Excel files allowed"}

        df = df.fillna("")
        stored_data = df.to_dict(orient="records")

        return {"data": stored_data}

    except Exception as e:
        return {"error": str(e)}

# GET → Get all data
@app.get("/data")
def get_data():
    return {"data": stored_data}

# PUT → Update a row
@app.put("/update/{index}")
def update_data(index: int, item: dict):
    try:
        stored_data[index] = item
        return {"message": "Updated successfully", "data": stored_data}
    except:
        return {"error": "Invalid index"}

# DELETE → Delete a row
@app.delete("/delete/{index}")
def delete_data(index: int):
    try:
        deleted = stored_data.pop(index)
        return {"message": "Deleted successfully", "deleted": deleted}
    except:
        return {"error": "Invalid index"}