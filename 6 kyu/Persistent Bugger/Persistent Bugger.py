#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def persistence(n, count=1):

    if len(str(n)) == 1:
        return 0

    base_list = [int(i) for i in str(n)]

    multiply_result = 1

    for x in base_list:
        multiply_result = multiply_result * x

    if len(str(multiply_result)) == 1:
        return count
    else:
        count += 1
        return persistence(multiply_result, count)