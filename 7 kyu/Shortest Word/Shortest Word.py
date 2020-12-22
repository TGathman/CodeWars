#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def find_short(s):

    temp = set()

    for i in s.split():
        temp.add(len(i))

    return min(temp)
