#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 20 March 2020


def get_sum(a, b):

    if a == b:

        return a

    return sum(range(b, a + 1)) if a > b else sum(range(a, b + 1))
