#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


from fastapi import FastAPI
from graphox.controllers import api_router
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
import time
from graphox import config
from graphox.helpers.requestvars import g
import ujson as json
import aiofiles
from graphox.config import FILEPATH

app = FastAPI(
    title="GRAPHOx",
    openapi_url=f"{config.API_V1_STR}/openapi.json",
    description="Micro serviço pesquisa de amigos",
    version="1.0.0",
    docs_url=None if not config.SWAGGER_DOCS else "/docs",
    redoc_url=None if not config.SWAGGER_DOCS else "/docs2",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    expose_headers=["X-Api-Key", "Authorization"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=config.API_V1_STR)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.on_event("startup")
async def startup():
    async with aiofiles.open(FILEPATH, "r") as tmp_file:
        # in Python3.6 + the dict keep the same order preserving aspect when created

        g().friends = json.loads(await tmp_file.read())


# @app.on_event("startup")
# def startup():
#     with open(FILEPATH, "r") as tmp_file:
#         g().friends = json.loads(tmp_file.read())


@app.on_event("shutdown")
async def shutdown():
    pass
