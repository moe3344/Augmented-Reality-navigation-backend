from app.utils.helper import validate_file_type
from fastapi import APIRouter, File, UploadFile

# Define the router object
router = APIRouter()



@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    validate_file_type(file.filename, ["jpg", "png"])
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}
