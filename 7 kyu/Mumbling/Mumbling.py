#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def accum(s):

    solution = ''

    for i in range(len(s)):
        solution += s[i] * (i + 1) + "-"

    return solution.title()[:-1]
