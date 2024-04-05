from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config.tags_metadata import tags_metadata

from app.routes import api_router

app = FastAPI (
  title="SKETCHIFY API",
  summary="Convert Image Into Sketch using Python",
  version="1.0.0",
  contact={
    "name": "Allan Foppa",
    "email": "allanfoppa.dev@gmail.com",
  },
  openapi_tags=tags_metadata
)

app.add_middleware (
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(api_router)
