# Python 3.8, 22 March 2020


def send_message(message):

    dict = {'.': '1',
            ',': '11',
            '?': '111',
            '!': '1111',
            'a': '2',
            'b': '22',
            'c': '222',
            'd': '3',
            'e': '33',
            'f': '333',
            'g': '4',
            'h': '44',
            'i': '444',
            'j': '5',
            'k': '55',
            'l': '555',
            'm': '6',
            'n': '66',
            'o': '666',
            'p': '7',
            'q': '77',
            'r': '777',
            's': '7777',
            't': '8',
            'u': '88',
            'v': '888',
            'w': '9',
            'x': '99',
            'y': '999',
            'z': '9999',
            ' ': '0',
            '\'': '*',
            '-': '**',
            '+': '***',
            '=': '****',
            '1': '1-',
            '2': '2-',
            '3': '3-',
            '4': '4-',
            '5': '5-',
            '6': '6-',
            '7': '7-',
            '8': '8-',
            '9': '9-',
            '0': '0-',
            '#': '#-',
            '*': '*-'}

    phone = ''
    upper = False

    for i in message:
        if upper is False and i.isupper():
            phone += f'#{dict[i.lower()]}'
            upper = True
        elif upper is True and i.islower():
            phone += f'#{dict[i]}'
            upper = False
        else:
            if len(phone) > 0 and phone[-1] == dict[i.lower()][0]:
                phone += f' {dict[i.lower()]}'
            else:
                phone += dict[i.lower()]

    return phone
