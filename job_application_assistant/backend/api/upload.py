from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

UPLOAD_DIR = "job_application_assistant/backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"status": "Resume uploaded", "file_path": file_path}
