from src.application.rest.app_fucture import FastAPIServer
import uvicorn


app = FastAPIServer()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
