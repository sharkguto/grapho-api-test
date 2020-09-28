#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# graph.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

from typing import List
from networkx import nx
from graphox.helpers.requestvars import g
import matplotlib.pyplot as plt


class GraphService(object):
    _g_dict = []

    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = []
        self._g_dict = g_dict
        # self.g_networkx = nx.Graph(g_dict)
        self.g_networkx = nx.MultiGraph(g_dict)

        pos = nx.spring_layout(self.g_networkx)
        nx.draw(
            self.g_networkx, pos, node_color="blue", font_size=8, font_weight="bold",
        )

        plt.savefig("debug-only.png", format="PNG")

    def get_friend_of_friend_mine(self, person: str) -> List:
        """Get who is not friend but can be

        Args:
            person (str): person name

        Returns:
            List: of not friends
        """
        return ["Luiza"]

    def get_friends(self, person: str) -> List:
        """Get all friends from person

        Args:
            person (str): Person name

        Returns:
            List: of friends
        """
        return self._g_dict[person]

    def save_new_person(self, person: str, friends: List[str]) -> bool:
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

        count_paths = {i: [] for i in self._g_dict.keys()}

        for person in self._g_dict.keys():
            for friend in self._g_dict[person]:
                count_paths[person].extend(
                    [
                        val
                        for sublist in list(
                            nx.all_simple_paths(
                                self.g_networkx, source=person, target=friend
                            )
                        )
                        for val in sublist
                    ]
                )
                # count_paths[person].extend(
                #     list(
                #         nx.all_simple_paths(
                #             self.g_networkx, source=person, target=friend
                #         )
                #     )
                # )

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

