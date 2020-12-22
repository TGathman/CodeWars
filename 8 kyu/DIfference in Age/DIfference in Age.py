#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 18 March 2020


def difference_in_ages(ages):

    return (min(ages), max(ages), max(ages) - min(ages))


# def difference_in_ages(ages):
#
#     if ages[0] < ages[1]:
#         new_array = [ages[0], ages[1]]
#     else:
#         new_array = [ages[1], ages[0]]
#
#     for i in ages[2:]:
#         if i < new_array[0]:
#             new_array[0] = i
#         if i > new_array[1]:
#             new_array[1] = i
#
#     new_array.append(new_array[1] - new_array[0])
#
#     return tuple(new_array)