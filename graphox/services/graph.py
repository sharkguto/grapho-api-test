#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# graph.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


class GraphService(object):
    _g_dict = []

    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = []
        self._g_dict = g_dict

    def get_people(self):
        return list(self._g_dict.keys())

