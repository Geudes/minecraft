from server.src.application.interface.server import IServerService
from server.src.application.use_case.server import ServerService
from server.src.core.database.di import db


def get_server_service() -> IServerService:
    return ServerService(provider=db)
