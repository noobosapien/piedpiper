from fastapi import FastAPI
import logging
import logging.config
from app.routers import storyboard_routes
from app.routers import test_routes

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(
    storyboard_routes.router, prefix="/api/storyboard", tags=["Storyboard"]
)

app.include_router(test_routes.router, tags=["Test"])
