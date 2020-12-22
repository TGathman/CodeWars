#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def getCount(inputStr):

    num_vowels = 0

    for i in inputStr:
        if i in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1

    return num_vowels
