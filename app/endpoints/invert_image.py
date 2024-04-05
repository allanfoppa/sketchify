from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
from app.controller.invert_image import InvertImageController
import io

router = APIRouter()

@router.post("/invert-image", tags=["invert-image"])
async def invert_image(file: UploadFile) -> bytes:
  try:
    contents = await file.read()
    processed_image = InvertImageController.process_image(contents)
    return StreamingResponse(io.BytesIO(processed_image), media_type="image/png")
  except Exception as e:
    return {"error": str(e)}

