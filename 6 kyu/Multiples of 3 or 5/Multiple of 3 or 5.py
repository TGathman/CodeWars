#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def solution(number):

    if number < 3:
        return 0

    results = set()

    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            results.add(i)

    return sum(results)
