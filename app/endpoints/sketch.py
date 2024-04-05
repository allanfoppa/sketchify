from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
from app.controller.sketch import SketchImageController
import io

router = APIRouter()

@router.post("/sketch", tags=["sketch"])
async def sketch(file: UploadFile) -> bytes:
  try:
    contents = await file.read()
    processed_image = SketchImageController.process_image(contents)
    return StreamingResponse(io.BytesIO(processed_image), media_type="image/png")
  except Exception as e:
    return {"error": str(e)}

