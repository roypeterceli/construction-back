from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from requests import HTTPError
from starlette.status import HTTP_200_OK

from app.config.logger_config import log
from app.exceptions.not_found_exception import NotFoundException
from app.schemas.api_response import ApiResponse


def add_global_exception_handler(app: FastAPI) -> None:
    """
    Register all exception handlers globally for the FastAPI app.
    """

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        log.error(f"HTTPException: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content=ApiResponse.error(exc.detail).model_dump()
        )

    @app.exception_handler(HTTPError)
    async def http_exception_handler(request: Request, exc: HTTPError):
        return JSONResponse(
            status_code=exc.response.status_code,
            content=exc.response.json()
        )

    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(request: Request, exc: NotFoundException):
        log.error(f"NotFoundException: {exc.message}")
        return JSONResponse(
            status_code=HTTP_200_OK,
            content=ApiResponse.error(exc.message).model_dump()
        )
