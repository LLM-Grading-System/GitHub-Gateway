import logging

from fastapi import FastAPI

from src.infrastructure.fastapi import add_custom_docs_endpoints, add_exception_handler, add_cors
from src.api.endpoints import router

logging.basicConfig(level=logging.INFO)


def create_application() -> FastAPI:
    application = FastAPI(title="GitHub Gateway", version="0.0.1", docs_url=None, redoc_url=None)
    add_custom_docs_endpoints(application)
    add_exception_handler(application)
    add_cors(application)
    application.include_router(router, prefix="/api")
    return application


app = create_application()
