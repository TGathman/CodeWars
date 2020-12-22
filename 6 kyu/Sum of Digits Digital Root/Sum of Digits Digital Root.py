#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def digital_root(n):

    if n < 10:

        return n

    root = 0

    for i in str(n):
        root += int(i)

    return digital_root(root)
