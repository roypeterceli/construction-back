from typing import TypeVar, ContextManager

from app.config.database_config import SessionLocal

from app.repositories.ubigeo_repository import UbigeoRepository
from app.services.ubigeo_service import UbigeoService

T = TypeVar("T")


class ServiceProvider:
    def __init__(self):
        self.db_session = SessionLocal

    def _get_service(self, service_class, repository_classes) -> ContextManager[T]:
        session = self.db_session()
        repos = [repo_class(session) for repo_class in repository_classes]
        service = service_class(*repos)

        class ServiceContextManager(ContextManager):
            def __enter__(self):
                return service

            def __exit__(self, exc_type, exc_val, exc_tb):
                session.close()

        return ServiceContextManager()

    def ubigeo_service(self) -> ContextManager[UbigeoService]:
        return self._get_service(UbigeoService, [UbigeoRepository])


service_provider = ServiceProvider()
