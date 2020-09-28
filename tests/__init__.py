#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


from graphox.helpers.requestvars import g
from fastapi.testclient import TestClient
from graphox.config import FILEPATH
import ujson as json
from graphox import app

client = TestClient(app)

# force load of json to global object in context
with open(FILEPATH, "r") as tmp_file:
    g().friends = json.loads(tmp_file.read())
