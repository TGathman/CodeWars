# Python 3.8, 20 March 2020.


def is_isogram(string):

    for i in string.lower():
        if string.lower().count(i) > 1:
            return False
    return True
