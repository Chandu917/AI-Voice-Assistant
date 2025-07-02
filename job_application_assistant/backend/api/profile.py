from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import shutil
import os

router = APIRouter()

PROFILE_STORAGE = "data/profile"
os.makedirs(PROFILE_STORAGE, exist_ok=True)

class Profile(BaseModel):
    name: str
    phone: str
    email: str
    linkedin: str = None
    github: str = None
    skills: list[str] = []
    experience: str = None
    job_preferences: dict = {}

profile_data = {}

@router.post("/create")
async def create_profile(
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    linkedin: str = Form(None),
    github: str = Form(None),
    skills: str = Form(""),
    experience: str = Form(None),
    job_preferences: str = Form("{}"),
    resume: UploadFile = File(None),
    cover_letter: UploadFile = File(None),
    certificates: UploadFile = File(None),
):
    global profile_data
    profile_data = {
        "name": name,
        "phone": phone,
        "email": email,
        "linkedin": linkedin,
        "github": github,
        "skills": skills.split(",") if skills else [],
        "experience": experience,
        "job_preferences": job_preferences,
    }

    # Save uploaded files
    if resume:
        resume_path = os.path.join(PROFILE_STORAGE, "resume_" + resume.filename)
        with open(resume_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)
        profile_data["resume_path"] = resume_path

    if cover_letter:
        cover_letter_path = os.path.join(PROFILE_STORAGE, "cover_letter_" + cover_letter.filename)
        with open(cover_letter_path, "wb") as buffer:
            shutil.copyfileobj(cover_letter.file, buffer)
        profile_data["cover_letter_path"] = cover_letter_path

    if certificates:
        certificates_path = os.path.join(PROFILE_STORAGE, "certificates_" + certificates.filename)
        with open(certificates_path, "wb") as buffer:
            shutil.copyfileobj(certificates.file, buffer)
        profile_data["certificates_path"] = certificates_path

    return JSONResponse(content={"message": "Profile created/updated successfully", "profile": profile_data})

@router.get("/get")
async def get_profile():
    if not profile_data:
        return JSONResponse(content={"message": "No profile found"}, status_code=404)
    return profile_data
