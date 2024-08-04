from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from source.config.config import Config, ConfigMiddleware
from source.config.routes import RoutesConfig
from source.database.core import create_all_tabels

from source.routes.root import router as root_router
from source.routes.register import router as register_router
from source.routes.token import router as token_router
from source.routes.user import router as user_router

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

routes = RoutesConfig

app.include_router(root_router, tags=['root'])
app.include_router(register_router, prefix=routes.register, tags=['register'])
app.include_router(token_router, prefix=routes.token, tags=['token'])
app.include_router(user_router, prefix=routes.user, tags=['users'])
