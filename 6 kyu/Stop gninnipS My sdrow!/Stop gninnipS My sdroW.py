#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 19 March 2020


def spin_words(sentence):

    return ' '.join(i if len(i) < 5 else i[::-1] for i in sentence.split())


# def spin_words(sentence):
#     word_list = sentence.split()
#     reverse_list = []
#     for i in range(len(word_list)):
#         if len(word_list[i]) < 5:
#             reverse_list.append(word_list[i])
#         else:
#             reverse_list.append(word_list[i][::-1])
#     return ' '.join(i for i in reverse_list)
