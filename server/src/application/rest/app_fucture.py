from fastapi import FastAPI
from src.application.rest.routing import router
from fastapi.middleware.cors import CORSMiddleware


def FastAPIServer() -> FastAPI:
    app = FastAPI(
        title="minecraft_servers",
        redoc_url=None
    )

    app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
