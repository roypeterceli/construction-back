from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import TypeVar, Generic, List, Optional, Type

from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate

T = TypeVar('T')
ID = TypeVar('ID')


class BaseRepository(Generic[T, ID]):
    def __init__(self, session: Session, model: Type[T]):
        """
        :param session: SQLAlchemy Session instance.
        :param model: SQLAlchemy model class (e.g., User, Product).
        """
        self.session = session
        self.model = model

    def save(self, instance: T) -> T:
        """Saves or updates an instance in the database."""
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def find_by_id(self, _id: ID) -> Optional[T]:
        """
        Finds an entity by its ID.
        :param _id: Primary ID of the entity.
        :return: The found instance or None if it doesn't exist.
        """
        return self.session.get(self.model, _id)

    def find_all(self) -> List[T]:
        """Returns all instances of the model."""
        return self.session.query(self.model).all()

    def update(self, instance: Optional[T] = None, _id: Optional[ID] = None, fields: Optional[dict] = None) -> Optional[
        T]:
        """
        Updates an entity in the database.

        :param instance: The instance to update (object-based update).
        :param _id: The ID of the entity to update (for direct update).
        :param fields: Dictionary with fields and values to update (for direct update).
        :return: The updated instance or None if not found.
        """
        if instance:
            # Object based update
            self.session.commit()
            self.session.refresh(instance)
            return instance

        if _id and fields:
            # Direct update in the database
            stmt = update(self.model).where(self.model.id == _id).values(**fields)
            self.session.execute(stmt)
            self.session.commit()
            return self.find_by_id(_id)

        raise ValueError("An instance or _id with fields must be provided to update")

    def delete(self, instance: T) -> None:
        """
        Deletes a specific instance from the database.
        :param instance: The model instance to delete.
        """
        self.session.delete(instance)
        self.session.commit()

    def delete_by_id(self, _id: ID) -> None:
        """
        Finds and deletes an entity by its ID.
        :param _id: Primary ID of the entity.
        """
        instance = self.find_by_id(_id)
        if instance:
            self.delete(instance)
        else:
            raise NoResultFound(f"Entity with ID {_id} not found.")

    def count(self) -> int:
        """Returns the total count of entities in the table."""
        return self.session.query(self.model).count()

    def exists_by_id(self, _id: ID) -> bool:
        """
        Checks if an entity exists with the given ID.
        :param _id: Primary ID of the entity.
        :return: True if it exists, False otherwise.
        """
        return self.session.query(self.model).filter_by(id=_id).first() is not None

    def find_all_paginated(self, params: Params) -> Page[T]:
        """
        Returns a paginated list of model records.
        Applies pagination parameters to the base query to efficiently handle large datasets.
        :param params: Pagination parameters (page number and size).
        :return: Page[T]: A paginated result including metadata.
        """
        return paginate(self.session.query(self.model), params)
