from fastapi import FastAPI
import logging
import logging.config
from app.routers import storyboard_routes

from app.routers import test_routes
from fastapi.middleware.cors import CORSMiddleware

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    storyboard_routes.router, prefix="/api/storyboard", tags=["Storyboard"]
)

app.include_router(test_routes.router, tags=["Test"])
