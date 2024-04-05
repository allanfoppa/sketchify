from app.helpers.image_processor import ImageProcessor
import cv2 as cv

class BlurImageController:

  def __init__(self) -> None:
    pass

  def process_image(contents: bytes) -> bytes:
    decode = ImageProcessor.decode(contents)

    blur_image = cv.GaussianBlur(decode, (21, 21), 0)

    _, img_encoded = cv.imencode('.png', blur_image)
    return img_encoded.tobytes()

