from fastapi import HTTPException, status

class ExceptionsBase(HTTPException):
    status_code: str = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "INTERNAL SERVER ERROR"

    def __init__(self, detail: str | None = None, status_code: str | None = None):
        super().__init__(
            detail=detail or self.status_code,
            status_code=status_code or self.status_code
        )
