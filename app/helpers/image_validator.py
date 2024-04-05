from fastapi.responses import JSONResponse

class ImageValidator:
  """Class for validating image uploads."""

  def validate_size(self, size) -> JSONResponse | None:
    """
    Validates if the uploaded image has a size greater than 0.

    Args:
      file (UploadFile): The uploaded image file.

    Returns:
      JSONResponse | None: A JSON response indicating an error if the image size is 0. None otherwise.
    """

    if size == 0:
      return JSONResponse(
        status_code=422,
        content={"error": "Invalid file. Please upload an image."}
      )

    return None
