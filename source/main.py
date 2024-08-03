from contextlib import asynccontextmanager
from fastapi import FastAPI
from source.config.config import Config, ConfigMiddleware
from fastapi.middleware.cors import CORSMiddleware

from source.database.core import create_all_tabels
from source.routes.root import router as root_router

Config = Config()
ConfigMiddleware = ConfigMiddleware()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tabels()
    yield

app = FastAPI(
    title=Config.title,
    description=Config.description,
    version=Config.description,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ConfigMiddleware.allow_origins,
    allow_credentials=ConfigMiddleware.allow_credentials,
    allow_methods=ConfigMiddleware.allow_methods,
    allow_headers=ConfigMiddleware.allow_headers,
)

app.include_router(root_router)
