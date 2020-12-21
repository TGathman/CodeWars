# Python 3.8, 20 march 2020


def pig_it(text):

    punc = ["!", ".", "?"]

    return " ".join(i[1:] + i[0] + "ay" if i not in punc else i for i in text.split())
