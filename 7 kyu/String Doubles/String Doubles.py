# Pyhton 3.8, 26 September 2020


from itertools import groupby


def doubles(text):

    if len(text) == 0:
        return ''

    if len(text) == 1:
        return text

    if len(text) == 2:
        return '' if text[0] == text[1] else text

    else:
        new_text = ''

        for key, group in groupby(text):
            if len(list(group)) % 2 != 0:
                new_text += key[0]

        if len(new_text) == len(text):
            return text

        else:
            return doubles(new_text)