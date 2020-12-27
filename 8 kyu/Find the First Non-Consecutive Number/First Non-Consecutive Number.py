#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 26 February 2020


def first_non_consecutive(arr):

    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i + 1]

    return None
