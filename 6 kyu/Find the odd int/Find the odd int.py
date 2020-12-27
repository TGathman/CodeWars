#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def find_it(seq):

    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
