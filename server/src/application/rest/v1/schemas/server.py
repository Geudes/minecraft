from enum import Enum
from pydantic import HttpUrl, Field, IPvAnyAddress, constr
from server.src.application.rest.schemas import BaseDTO, PaginationDTO


class ServerStatus(Enum):
    ONLINE = "online"
    OFFLINE = "offline"


class ServerDTO(BaseDTO):
    id: int
    img_url: HttpUrl | None
    name: str
    domain: str
    ip_address: IPvAnyAddress
    port: int
    version: str
    max_players: int
    online_players: int
    status: ServerStatus
    type: str


class CreateServerDTO(BaseDTO):
    img_url: HttpUrl | None = Field(default=None)
    name: str = Field(min_length=5, max_length=100)
    domain: str
    ip_address: IPvAnyAddress
    port: int = Field(default=25565)
    version: constr(pattern=r'^\d+\.\d+(\.\d+)?$')
    max_players: int = Field(ge=1)
    online_players: int = Field(ge=0)
    status: ServerStatus = Field(default=ServerStatus.ONLINE)
    type: str


class UpdateServerDTO(BaseDTO):
    img_url: HttpUrl | None = Field(default=None)
    name: str | None = Field(min_length=5, max_length=100)
    domain: str | None
    ip_address: IPvAnyAddress | None
    port: int | None
    version: constr(pattern=r'^\d+\.\d+(\.\d+)?$') | None
    max_players: int = Field(ge=1) | None
    online_players: int = Field(ge=0) | None
    status: ServerStatus | None
    type: str | None


class FetchListParamsDTO(PaginationDTO):
    pass
