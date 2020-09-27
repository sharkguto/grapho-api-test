#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# requestvars.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


import contextvars
import types


request_global = contextvars.ContextVar(
    "request_global", default=types.SimpleNamespace()
)


def g():
    return request_global.get()
