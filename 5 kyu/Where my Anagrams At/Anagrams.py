#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 23 February 2020


def anagrams(word, words):

    # Deletes words from words list that aren't equal in length to word.
    # Starts at end of list to avoid index errors.

    for i in range(len(words) - 1, -1, -1):
        if len(words[i]) != len(word):
            del words[i]

    # Compares character count by word in words list.
    # Starts at end of list to avoid index errors.

    for i in range(len(words) - 1, -1, -1):
        for j in word:
            if word.count(j) != words[i].count(j):
                del words[i]
                break

    return words
