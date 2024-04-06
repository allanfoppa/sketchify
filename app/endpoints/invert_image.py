from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from app.controller.invert_image import InvertImageController
from app.helpers.streaming_return import StreamingReturn
from app.helpers.image_validator import ImageValidator

router = APIRouter()


@router.post("/invert-image", tags=["invert-image"])
async def invert_image(file: UploadFile) -> bytes:
  try:

    error_response = ImageValidator().validate_size(file.size)
    if error_response:
      return error_response

    contents = await file.read()
    processed_image = InvertImageController.process_image(contents)
    return StreamingReturn.converted_image(processed_image)
  except Exception as e:
    return JSONResponse(status_code=500, content={"error": str(e)})

