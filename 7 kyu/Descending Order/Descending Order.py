#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 19 March 2020


def descending_order(num):

    reverse_list = sorted(str(num), reverse=True)

    return int("".join(i for i in reverse_list))
