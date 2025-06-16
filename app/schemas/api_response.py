from typing import Generic, TypeVar, Optional

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    status: bool
    message: str
    data: Optional[T] = None

    @staticmethod
    def ok(data: Optional[T] = None) -> "ApiResponse":
        """
        Success response
        :param data: The data to return (optional).
        :return: An ok ApiResponse.
        """
        return ApiResponse(status=True, message="OK", data=data)

    @staticmethod
    def error(message: str, data: Optional[T] = None) -> "ApiResponse":
        """
        Error response.
        :param message: The error message.
        :param data: Additional data for the error response (optional).
        :return: An error ApiResponse.
        """
        return ApiResponse(status=False, message=message, data=data)
