#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 29 December 2020


def valid_solution(board):
    """
    Checks validity of Sudoku solution. Input is 9x9 2d array containing integers 0 - 9.
    Returns True if valid, false if not. If solution contains 0, it's invalid.
    Based on premise all rows, columns, and 3x3 sub-arrays will be sets of length 9 in valid solutions.
    """

    # Checks rows.

    for row in board:
        if len(set(row)) != 9 or 0 in row:
            return False

    # Checks columns.

    for row in [[row[column] for row in board] for column in range(9)]:
        if len(set(row)) != 9 or 0 in row:
            return False

    # Checks blocks.

    block_count = 0
    min_1, max_1, min_2, max_2 = 0, 3, 0, 3

    while block_count < 9:

        temp = []

        for i in range(min_1, max_1):
            for j in range(min_2, max_2):
                temp.append(board[i][j])

        if len(set(temp)) != 9 or 0 in row:
            return False

        if max_2 == 9:
            min_2, max_2 = 0, 3
            min_1 += 3
            max_1 += 3
        else:
            min_2 += 3
            max_2 += 3

        block_count += 1

    return True
