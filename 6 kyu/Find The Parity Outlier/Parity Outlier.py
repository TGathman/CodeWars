#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 19 March 2020


def find_outlier(integers):

    mod_str = ''.join(str(i % 2) for i in integers)

    return integers[mod_str.index("1")] if mod_str.count("0") > 1 else integers[mod_str.index("0")]