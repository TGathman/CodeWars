# Python 3.8, 25 March 2020


def greatest_product(n):

    prod = int(n[0:1]) * int(n[1:2]) * int(n[2:3]) * int(n[3:4]) * int(n[4:5])

    while len(n) > 5:
        n = n[1:]
        if int(n[0:1]) * int(n[1:2]) * int(n[2:3]) * int(n[3:4]) * int(n[4:5]) > prod:
            prod = int(n[0:1]) * int(n[1:2]) * int(n[2:3]) * int(n[3:4]) * int(n[4:5])

    return prod
