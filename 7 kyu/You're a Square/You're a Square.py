#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


from math import sqrt


def is_square(n):

    return n >= 0 and sqrt(n).is_integer()
