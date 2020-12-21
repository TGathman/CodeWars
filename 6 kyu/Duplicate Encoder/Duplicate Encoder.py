# Python 3.8, 20 march 2020


def duplicate_encode(word):

    return "".join("(" if word.lower().count(i) == 1 else ")" for i in word.lower())
