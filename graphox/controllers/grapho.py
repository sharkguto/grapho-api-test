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


@router.get("/friends", tags=["friends"])
async def get_kpis_fornec(response: Response):
    """
    Get all friends and return who have more friends first
    [Ana, Maria, Vinicius, Luiza, João, Carlos]
    math: n(n-1)/2
    """

    # g().friends.keys()
    # g().friends.items()

    # sorted_by_name_seq = {
    #     k: v for k, v in sorted(g().friends.items(), key=lambda item: item[0])
    # }

    # data = sorted(
    #     sorted_by_name_seq,
    #     key=lambda item: (
    #         (len(sorted_by_name_seq[item]) - 1) * len(sorted_by_name_seq[item])
    #     )
    #     / 2,
    #     reverse=True,
    # )
    graph_svc = GraphService(g().friends)

    return graph_svc.get_people()

    # g().friends.items()

    # sorted_by_name_seq = sorted(g().friends, key=lambda key: len(g().friends[key]))

    # data = sorted(
    #     sorted_by_name_seq, key=lambda item: len(sorted_by_name_seq[item]), reverse=True
    # )

    # counter_dict = {i: 0 for i in g().friends.keys()}

    # for person in g().friends.keys():

    #     for i in g().friends[person]:
    #         if person in g().friends[i]:
    #             for ii in g().friends[i]:
    #                 if ii != person:
    #                     counter_dict[person] += 1

    # return list(g().friends.keys())

    # return data

