#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 9 February 2020


def snail(snail_map):

    if snail_map == []:
        return []

    return [snail_map[0][i] for i in range(0, len(snail_map[0]))] + \
           [snail_map[i][len(snail_map) - 1] for i in range(1, len(snail_map))] + \
           [snail_map[len(snail_map)-1][i] for i in range(len(snail_map) - 2, -1, -1)] + \
           [snail_map[i][0] for i in range(len(snail_map) - 2, 0, -1)] + snail([i[1:-1] for i in snail_map[1:-1]])
