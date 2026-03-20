from src.application.exceptions.http.base import ExceptionsBase, status

class ServerException(ExceptionsBase):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Ошибка на стороне сервера"

class ServiceUnavailableException(ExceptionsBase):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    detail = "Сервис временно недоступен"