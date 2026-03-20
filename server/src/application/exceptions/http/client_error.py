from src.application.exceptions.http.base import ExceptionsBase, status


class BadRequestException(ExceptionsBase):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Некорректный запрос"


class NotAuthenticatedException(ExceptionsBase):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не авторизован"


class PermissionDeniedException(ExceptionsBase):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Доступ запрещен"


class NotFoundException(ExceptionsBase):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Ресурс не найден"


class ConflictException(ExceptionsBase):
    status_code = status.HTTP_409_CONFLICT
    detail = "Конфликт данных (например, такой email уже есть)"
