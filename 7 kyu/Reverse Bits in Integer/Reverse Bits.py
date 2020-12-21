# Python 3.8, 29 June 2020


def reverse_bits(n):

    return int(bin(n).replace('0b', '')[::-1], 2)
