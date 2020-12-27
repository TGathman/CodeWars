#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 9 February 2020


def alphabet_position(text):

    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_dict = {}
    position = 1
    substitution = ""

    for i in alphabet_list:
        alphabet_dict[i] = position
        position += 1

    lower_string = text.lower()

    for j in lower_string:
        if j in alphabet_dict:
            substitution += str(alphabet_dict[j]) + " "

    substitution = substitution.strip()

    return substitution
