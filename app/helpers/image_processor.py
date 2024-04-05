import cv2 as cv
import numpy as np

class ImageProcessor:

  def __init__(self) -> None:
    pass

  def decode(contents: bytes) -> bytes:
    """
    This line converts the contents variable, which is a bytes-like
    object into a NumPy array of type uint8. The np.frombuffer
    function creates a NumPy array from the raw data stored in
    the contents object.
    """
    nparr = np.frombuffer(contents, np.uint8)

    """
    Decodes the NumPy array 'nparr' into an image using OpenCV's imdecode
    function. The cv.IMREAD_COLOR flag specifies that the image should
    be loaded in color mode with three color channels: red, green, and blue.
    """
    image = cv.imdecode(nparr, cv.IMREAD_COLOR)

    """
    Return decoded image
    """
    return image
