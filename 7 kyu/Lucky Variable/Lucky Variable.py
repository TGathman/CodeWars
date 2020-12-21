# Python 3.8, 27 September 2020


def find_variable():

    for var in globals():
        if eval(var) == 777:
            return var
