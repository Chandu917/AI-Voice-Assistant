from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def get_applications():
    return {"message": "Applications endpoint placeholder"}

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def get_applications():
    return {"message": "Applications endpoint placeholder"}

@router.post("/auto-apply")
async def auto_apply(request: Request):
    try:
        data = await request.json()
        if not data:
            return JSONResponse(content={"status": "error", "message": "No application data provided"}, status_code=400)
        # Here you would call the actual job application workflow or service
        # For now, simulate success with detailed logging
        print(f"Received auto-apply request with data: {data}")
        # Validate required fields in data
        if "command_text" not in data or "user_profile" not in data or "resume_path" not in data:
            return JSONResponse(content={"status": "error", "message": "Missing required fields in request data"}, status_code=400)
        # Import and call workflow function
        from backend.services.workflow import run_job_application_workflow
        result = run_job_application_workflow(
            data["command_text"],
            data["user_profile"],
            data["resume_path"],
            data.get("cover_letter_path")
        )
        return JSONResponse(content={"status": "success", "message": "Application submitted", "result": result})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
