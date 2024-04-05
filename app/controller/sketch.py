from app.helpers.image_processor import ImageProcessor
import cv2 as cv

class SketchImageController:

  def __init__(self) -> None:
    pass

  def process_image(contents: bytes) -> bytes:
    decode = ImageProcessor.decode(contents)
    gray_image = cv.cvtColor(decode, cv.COLOR_BGR2GRAY)
    invert_image = cv.bitwise_not(gray_image)
    blur_image = cv.GaussianBlur(invert_image, (21, 21), 0)
    invert_blur = cv.bitwise_not(blur_image)
    sketch = cv.divide(gray_image, invert_blur, scale=256.0)

    _, img_encoded = cv.imencode('.png', sketch)
    return img_encoded.tobytes()

