#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# grapho.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


from fastapi import APIRouter, HTTPException
from graphox.services.graph import GraphService
from starlette.responses import Response
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from graphox.helpers.requestvars import g

router = APIRouter()


@router.get("/friends/{person}", tags=["friends"])
async def get_kpis_fornec(
    response: Response, person: str = "Gustavo",
):
    """ 
    Get first connection friends from person
    """
    if not person:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST)
    if not person in g().friends.keys():
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    return {"person": g().friends[person]}


@router.get("/not-friends/{person}", tags=["not-friends"])
async def get_kpis_fornec(
    response: Response, person: str = "Gustavo",
):
    """ 
    Get first connection friends from person
    """
    if not person:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST)
    if not person in g().friends.keys():
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    return {"person": g().friends[person]}


@router.get("/friends", tags=["all"])
async def get_kpis_fornec(response: Response):
    """
    Expected result
    [Ana, Maria, Vinicius, Luiza, João, Carlos]
    """

    graph_svc = GraphService(g().friends)

    return graph_svc.get_people()

