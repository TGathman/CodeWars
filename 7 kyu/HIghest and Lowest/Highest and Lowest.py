#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def high_and_low(numbers):

    temp = [int(i) for i in numbers.split()]

    return f"{max(temp)} {min(temp)}"


# def high_and_low(numbers):
#     temp = []
#
#     for i in numbers.split():
#         temp.append(int(i))
#
#     return str(max(temp)) + " " + str(min(temp))
