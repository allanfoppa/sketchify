from fastapi.responses import StreamingResponse
import io

class StreamingReturn:
  """Class for returning processed images."""

  def converted_image(processed_image: bytes) -> StreamingResponse:
    """
    Gets the converted image and return .

    Args:
      processed_image (bytes): The converted image file.

    Returns:
      StreamingResponse
    """

    return StreamingResponse(io.BytesIO(processed_image), media_type="image/png")
