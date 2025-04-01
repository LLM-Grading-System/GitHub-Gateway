import logging

from fastapi import FastAPI

from src.infrastructure.fastapi import add_custom_docs_endpoints, add_exception_handler, add_cors
from src.api.router.rest_api_router import router as rest_api_router
from src.api.router.async_router import async_router

logging.basicConfig(level=logging.INFO)


def create_application() -> FastAPI:
    application = FastAPI(title="GitHub Gateway", version="0.0.1", docs_url=None, redoc_url=None)
    add_custom_docs_endpoints(application)
    add_exception_handler(application)
    add_cors(application)
    application.include_router(rest_api_router, prefix="/api")
    application.include_router(async_router)
    return application


app = create_application()
