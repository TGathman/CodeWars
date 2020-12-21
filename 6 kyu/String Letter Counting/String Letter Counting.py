# Python 3.8, 5 May 2020


def string_letter_count(s):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    stripped_string = ''.join([char for char in s if char.isalpha()]).lower()

    return ''.join([f'{stripped_string.count(char)}{char}' for char in alphabet if stripped_string.count(char) > 0])
