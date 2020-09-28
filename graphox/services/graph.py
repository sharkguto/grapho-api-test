#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# graph.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

from typing import List
from networkx import nx
from graphox.helpers.requestvars import g


class GraphService(object):
    _g_dict = []

    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = []
        self._g_dict = g_dict
        self.g_networkx = nx.Graph(g_dict)

    def save_new_person(self, person: str, friends: List[str]):
        """Save new person on dictonary

        Args:
            person (str): person first name
            friends (List[str]): list of friends
        """

        if person in friends:
            return False

        intersection = set(self._g_dict.keys()).intersection(set(friends))

        if len(friends) != len(intersection):
            return False

        self._g_dict[person] = friends
        g().friends = self._g_dict.copy()
        return True

    def get_people(self) -> List:
        """initial result: [Ana, Maria, Vinicius, Luiza, João, Carlos]

        I think i need to bring ordered people by number of paths first, and second by name
        Returns:
            List: all people
        """

        count_paths = {i: 0 for i in self._g_dict.keys()}

        for person in self._g_dict.keys():
            for friend in self._g_dict[person]:
                count_paths[person] += len(
                    list(
                        nx.all_simple_paths(
                            self.g_networkx, source=person, target=friend
                        )
                    )
                )

        # order_dict_paths = {i: [] for _, i in count_paths.items()}
        order_dict_paths = {
            f"{i}": set() for i in sorted(set(count_paths.values()), reverse=True)
        }

        # for k_tmp in

        for k, v in count_paths.items():
            order_dict_paths[f"{v}"].add(k)

        # sort_orders = sorted(order_dict_paths.items(), key=lambda x: x[1], reverse=True)

        # {f"{v}": map(lambda k: k,k) for k, v in count_paths.items()}

        return list(self._g_dict.keys())
        # list(self._g_dict.keys())

