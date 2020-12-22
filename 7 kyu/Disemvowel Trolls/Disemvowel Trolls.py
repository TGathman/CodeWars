#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def disemvowel(string):

    new_string = ''

    for i in string:
        if i.lower() not in 'aeiou':
            new_string += i

    return new_string
