# Python 3.8, 29 June 2020


def encrypt_this(text):

    string_split = text.split()

    encrypted = []

    for i in string_split:
        if len(i) == 1:
            encrypted.append(f'{ord(i[0])}')
        elif len(i) == 2:
            encrypted.append(f'{ord(i[0])}{i[1]}')
        elif len(i) == 3:
            encrypted.append(f'{ord(i[0])}{i[2]}{i[1]}')
        else:
            encrypted.append(f'{ord(i[0])}{i[-1]}{i[2:len(i) - 1]}{i[1]}')

    return ' '.join(encrypted)