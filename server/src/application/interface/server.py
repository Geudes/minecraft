from collections.abc import Sequence
from typing import Protocol
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from server.src.application.rest.v1.schemas.server import CreateServerDTO, UpdateServerDTO, \
    FetchListParamsDTO
from server.src.core.database.table import Server


class IServerService(Protocol):
    async def fetch_list(
        self, input_dto: FetchListParamsDTO
    ) -> Sequence[Server]: ...


    async def fetch_by_id(
        self, input_dto: UUID
    ) -> Server: ...

    async def create(
        self, input_dto: CreateServerDTO
    ) -> Server: ...

    async def update(
        self, input_dto: tuple[UUID, UpdateServerDTO]
    ) -> Server: ...

    async def delete(
        self, input_dto: UUID
    ) -> None: ...
