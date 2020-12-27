#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 26 February 2020


def solution(s):

    results = []

    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            results.append(s[i: i + 2])
    else:
        for i in range(0, len(s) - 2, 2):
            results.append(s[i: i + 2])
        a = s[-1] + "_"
        results.append(a)

    return results
