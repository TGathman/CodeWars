# Python 3.8, 26 September 2020


def solve(forward_string):

    reverse_string = list(forward_string[::-1].replace(' ', ''))

    for index, elem in enumerate(forward_string):
        if elem == ' ':
            reverse_string.insert(index, ' ')

    return ''.join(reverse_string)