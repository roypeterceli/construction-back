from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.cors import CORSMiddleware

from app.exceptions.exception_handler import add_global_exception_handler
from app.middlewares.logging_middleware import LoggingMiddleware
from app.routers.ubigeo_router import router as ubigeo_router
from app.routers.zone_router import router as zone_router
from app.routers.troncal_router import router as troncal_router
from app.routers.node_router import router as node_router
from app.routers.naps_router import router as naps_router
from app.routers.ports_router import router as ports_router


app = FastAPI(title="Construction UI DB")

Instrumentator().instrument(app).expose(app, include_in_schema=False)


""" Handlers """
add_global_exception_handler(app)


""" Middlewares """
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)


""" Routes """
app.include_router(ubigeo_router)
app.include_router(zone_router)
app.include_router(troncal_router)
app.include_router(node_router)
app.include_router(naps_router)
app.include_router(ports_router)

