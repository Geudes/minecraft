from collections.abc import Sequence
from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.params import Query

from server.src.application.interface.server import IServerService
from server.src.application.rest.di import get_server_service
from server.src.application.rest.v1.schemas.server import ServerDTO, FetchListParamsDTO, CreateServerDTO, \
    UpdateServerDTO

router = APIRouter(prefix="/servers", tags=["Server"])


@router.get(
    path="/",
    response_model=Sequence[ServerDTO],
    status_code=HTTPStatus.OK
)
async def fetch_list(
    params: FetchListParamsDTO = Query(),
    service: IServerService = Depends(get_server_service)
) -> Sequence[ServerDTO]:
    result = service.fetch_list(input_dto=params)
    return [ServerDTO.model_validate(result)]


@router.get(
    path="/{server_id}",
    response_model=ServerDTO,
    status_code=HTTPStatus.OK
)
async def fetch_by_id(
    server_id: UUID,
    service: IServerService = Depends(get_server_service)
) -> ServerDTO:
    result = service.fetch_by_id(input_dto=server_id)
    return ServerDTO.model_validate(result)


@router.post(
    path="/",
    response_model=ServerDTO,
    status_code=HTTPStatus.CREATED
)
async def create(
    create_data: CreateServerDTO,
    service: IServerService = Depends(get_server_service)
) -> ServerDTO:
    result = service.create(input_dto=create_data)
    return ServerDTO.model_validate(result)


@router.put(
    path="/{server_id}",
    response_model=ServerDTO,
    status_code=HTTPStatus.OK
)
async def update(
    server_id: UUID,
    update_data: UpdateServerDTO,
    service: IServerService = Depends(get_server_service)
) -> ServerDTO:
    result = service.update(
        input_dto=(server_id, update_data)
    )
    return ServerDTO.model_validate(result)


@router.delete(
    path="/{server_id}",
    response_model=ServerDTO,
    status_code=HTTPStatus.NO_CONTENT
)
async def delete(
    server_id: UUID,
    service: IServerService = Depends(get_server_service)
) -> ServerDTO:
    result = service.delete(input_dto=server_id)
    return ServerDTO.model_validate(result)
