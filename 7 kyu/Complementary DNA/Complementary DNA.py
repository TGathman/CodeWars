#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 19 March 2020


def DNA_strand(dna):

    dna_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    return ''.join(dna_dict[i] for i in dna)
