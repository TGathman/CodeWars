#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 29 December 2020


def solution(string: str, markers: list) -> str:
    """
    Strips a string given a list of markers.
    """

    # Splits string on newline, checks each line for markers, splits if found. Splices back together via newline.

    split_string = string.split('\n')

    for idx in range(len(split_string)):
        for marker in markers:
            if marker in split_string[idx]:
                split_string[idx] = split_string[idx].split(marker)[0].strip()

    return '\n'.join(split_string)
