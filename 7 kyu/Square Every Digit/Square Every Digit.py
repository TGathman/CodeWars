#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def square_digits(num):

    return int("".join(str(int(i)**2) for i in str(num)))
