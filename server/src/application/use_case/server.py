from collections.abc import Sequence
from uuid import UUID
from sqlalchemy import select, delete, insert, update

from server.src.application.interface.server import IServerService
from server.src.application.rest.v1.schemas.server import CreateServerDTO, UpdateServerDTO, \
    FetchListParamsDTO
from server.src.core.database.di import DBProvaider
from server.src.core.database.table import Server


class ServerService(IServerService):

    def __init__(
        self, provider: DBProvaider
    ) -> None:
        self.session = provider.session

    async def fetch_list(
        self, input_dto: FetchListParamsDTO
    ) -> Sequence[Server]:
        query = (
            select(Server)
            .offset(input_dto.offset)
            .limit(input_dto.limit)
        )
        return (await self.session.scalars(query)).all()

    async def fetch_by_id(
        self, input_dto: UUID
    ) -> Server:
        query = (
            select(Server)
            .where(Server.id == input_dto)
        )
        return (await self.session.scalars(query)).one()

    async def create(
        self, input_dto: CreateServerDTO
    ) -> Server:
        stmt = (
            insert(Server)
            .values(
                input_dto.model_dump()
            )
            .returning(Server)
        )
        return (await self.session.scalars(stmt)).one()

    async def update(
        self, input_dto: tuple[UUID, UpdateServerDTO]
    ) -> Server:
        server_id, update_data = input_dto
        stmt = (
            update(Server)
            .where(Server.id == server_id)
            .values(**update_data.model_dump(
                exclude_unset=True
            ))
            .returning(Server)
        )
        return (await self.session.scalars(stmt)).one()

    async def delete(
        self, input_dto: UUID
    ) -> None:
        stmt = delete(Server).where(Server.id == input_dto)
        await self.session.execute(stmt)
