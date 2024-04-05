from app.helpers.image_processor import ImageProcessor
import cv2 as cv

class GrayImageController:

  def __init__(self) -> None:
    pass

  def process_image(contents: bytes) -> bytes:
    decode = ImageProcessor.decode(contents)
    gray_image = cv.cvtColor(decode, cv.COLOR_BGR2GRAY)

    _, img_encoded = cv.imencode('.png', gray_image)
    return img_encoded.tobytes()

