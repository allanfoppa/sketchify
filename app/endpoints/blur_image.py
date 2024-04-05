from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
from app.controller.blur_image import BlurImageController
import io

router = APIRouter()

@router.post("/blur-image", tags=["blur-image"])
async def blur_image(file: UploadFile) -> bytes:
  try:
    contents = await file.read()
    processed_image = BlurImageController.process_image(contents)
    return StreamingResponse(io.BytesIO(processed_image), media_type="image/png")
  except Exception as e:
    return {"error": str(e)}

