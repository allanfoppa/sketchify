from fastapi import APIRouter

from app.endpoints import gray_image
from app.endpoints import invert_image
from app.endpoints import blur_image
from app.endpoints import sketch

api_router = APIRouter()

api_router.include_router(gray_image.router)
api_router.include_router(invert_image.router)
api_router.include_router(blur_image.router)
api_router.include_router(sketch.router)
