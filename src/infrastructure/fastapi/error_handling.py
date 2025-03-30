from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.api.general_schemas import ErrorResponse
from src.services.exceptions import ServiceError


def add_exception_handler(application: FastAPI) -> None:
    @application.exception_handler(ServiceError)
    async def handle_application_error(_: Request, exc: ServiceError) -> JSONResponse:
        return JSONResponse(
            content=ErrorResponse(message=exc.message),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
