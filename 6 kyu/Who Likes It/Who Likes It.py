#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 19 March 2020


def likes(names):

    if names == []:
        return "no one likes this"

    if len(names) == 1:
        return f"{names[0]} likes this"

    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"

    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
