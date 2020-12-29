#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 27 December 2020


def validate_battlefield(field: list ) -> bool:
    """
    Validates a 10x10 Battleship with the following ship parameters: ships = 4, 3, 3, 2, 2, 2, 1, 1, 1 and
    no adjacency"""

    # Check validity of field (all ships add to 20).

    if sum(sum(field, [])) != 20:
        return False

    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    # Iterate through each coordinate left-to-right, top-to-bottom, on field and checks ship validity.

    for field_index, row in enumerate(field):
        for row_index, coordinate in enumerate(row):
            if coordinate == 1 and not ship_validator(field, field_index, row_index, ships):
                return False

    return True


def ship_validator(field: list, field_index: int, row_index: int, ships: list) -> bool:
    """Determines whether ship is positioned horizontally or vertically and validates using that parameter."""

    if row_index == 9:

        return validate_down(field, field_index, row_index, ships)

    if field_index == 9:

        return validate_horiz(field, field_index, row_index, ships)

    if field[field_index][row_index + 1] == 1 and field[field_index + 1][row_index] == 0:

        return validate_horiz(field, field_index, row_index, ships)

    if field[field_index][row_index + 1] == 0 and field[field_index + 1][row_index] == 1:

        return validate_down(field, field_index, row_index, ships)

    # Covers a ship length one not on row_index 9 or field_index 9. Validate_down covers necessary adjacency validation,
    # horizontal will not.

    return validate_down(field, field_index, row_index, ships)


def validate_down(field: list, field_index: int, row_index: int, ships: list) -> bool:
    """Validates a vertical ship by checking adjacency validity and removing ship to prevent duplication."""

    length = 0
    current_coord = field[field_index][row_index]

    while current_coord == 1:

        # Since field is validated left-to-right, top-to-bottom, only need to ensure horizontal and down-diagonal
        # adjacents are not 1s as we move down the ship.

        validity_check = {(field_index, abs(row_index - 1)),
                          (field_index, row_index + 1),
                          (field_index + 1, abs(row_index - 1)),
                          (field_index + 1, row_index + 1)}

        for indices in validity_check:
            try:
                if field[indices[0]][indices[1]] == 1:
                    return False
            except IndexError:
                pass

        try:
            if field[field_index + 1][row_index] == 1:
                field[field_index][row_index] = 0
                length += 1
                field_index += 1
                current_coord = field[field_index][row_index]
            else:
                field[field_index][row_index] = 0
                length += 1
                current_coord = field[field_index][row_index]
        except IndexError:
            field[field_index][row_index] = 0
            length += 1
            current_coord = field[field_index][row_index]

    if length in ships:
        ships.remove(length)
        return True
    else:
        return False


def validate_horiz(field: list, field_index: int, row_index: int, ships: list) -> bool:
    """Validates a horizontal ship by checking adjacency validity and removing ship to prevent duplication."""

    length = 0
    current_coord = field[field_index][row_index]

    while current_coord == 1:

        # Since field is validated left-to-right, top-to-bottom, only need to ensure vertical and right-diagonal
        # adjacents are not 1s as we move across the ship.

        validity_check = {(field_index + 1, row_index),
                          (field_index + 1, row_index + 1),
                          (abs(field_index - 1), row_index + 1),
                          (field_index + 1, abs(row_index - 1))}

        for indices in validity_check:
            try:
                if field[indices[0]][indices[1]] == 1:
                    return False
            except IndexError:
                pass

        try:
            if field[field_index][row_index + 1] == 1:
                field[field_index][row_index] = 0
                length += 1
                row_index += 1
                current_coord = field[field_index][row_index]
            else:
                field[field_index][row_index] = 0
                length += 1
                current_coord = field[field_index][row_index]
        except IndexError:
            field[field_index][row_index] = 0
            length += 1
            current_coord = field[field_index][row_index]

    if length in ships:
        ships.remove(length)
        return True
    else:
        return False
