#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 9 February 2020


def odd_row(n):

    if n == 1:
        return [n]

    if n > 1:
        a = n * (n - 1) + 1
        return [a + i for i in range(0, 2 * n, 2)]
