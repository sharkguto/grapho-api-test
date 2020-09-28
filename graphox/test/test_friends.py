#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_friends.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

from . import client


def test_list_people():
    response = client.get("/v1/friends")
    assert response.status_code == 200
    assert response.json() == ["Ana", "Maria", "Vinicius", "Luiza", "João", "Carlos"]


def test_list_friends_ana():
    response = client.get("/v1/friends/Ana")
    assert response.status_code == 200
    assert response.json() == ["Maria", "Vinicius", "João", "Carlos"]


def test_list_not_friends_ana():
    response = client.get("/v1/not-friends/Ana")
    assert response.status_code == 200
    assert response.json() == ["Luiza"]


def test_add_new_friend_to_ana():
    response = client.put("/v1/friends", params=dict(person="Gustavo", friends=["Ana"]))
    assert response.status_code == 201
    assert response.json() == {"success": True}
