from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.config.app_config import app_property
from app.config.logger_config import LoggerFactory


async def summarize_request(request: Request) -> dict:
    try:
        body = await request.body()
        try:
            body = body.decode("utf-8")
        except UnicodeDecodeError:
            pass
    except Exception:
        body = b"Unable to read body"

    return {
        "method": request.method,
        "url": str(request.url),
        "path": request.url.path,
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "client": {"host": request.client.host, "port": request.client.port},
        "cookies": request.cookies,
        "path_params": request.path_params,
        "body": body
    }


class LoggingMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)
        self.log = LoggerFactory.get_logger(f"{app_property.name}.request")

    async def dispatch(self, request: Request, call_next):
        request_summary = await summarize_request(request)
        self.log.info(f"API request: {request_summary}")
        response = await call_next(request)
        return response
