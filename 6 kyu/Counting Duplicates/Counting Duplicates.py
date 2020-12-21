# Python 3.8, 20 March 2020


def duplicate_count(text):

    str_dict = {i:text.lower().count(i) for i in text}
    occurrence = 0
    for i in str_dict:
        if str_dict[i] > 1:
            occurrence += 1
    return occurrence
