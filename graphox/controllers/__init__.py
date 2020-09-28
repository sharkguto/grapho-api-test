#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

from fastapi import APIRouter

from graphox.controllers import grapho


api_router = APIRouter()
#api_router.include_router(db_query.router, tags=["database"])
api_router.include_router(grapho.router, tags=["friends"])