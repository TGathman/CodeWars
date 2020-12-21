# Pyhton 3.8, 26 September 2020


def solve(num_list):

    odds = 0
    evens = 0

    for num in num_list:
        if type(num) == int and num % 2 == 0:
            evens += 1
        elif type(num) == int:
            odds += 1

    return evens - odds
