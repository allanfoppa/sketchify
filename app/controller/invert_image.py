from app.helpers.image_processor import ImageProcessor
import cv2 as cv

class InvertImageController:

  def __init__(self) -> None:
    pass

  def process_image(contents: bytes) -> bytes:
    decode = ImageProcessor.decode(contents)

    invert_image = cv.bitwise_not(decode)

    _, img_encoded = cv.imencode('.png', invert_image)
    return img_encoded.tobytes()

