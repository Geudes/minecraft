from pydantic import BaseModel, ConfigDict, Field


class BaseDTO(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )


class PaginationDTO(BaseDTO):
    limit: int = Field(ge=10, le=100, default=10)
    offset: int = Field(ge=0, le=100, default=0)
