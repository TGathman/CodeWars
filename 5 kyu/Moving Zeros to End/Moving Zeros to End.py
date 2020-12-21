# Python 3.8, 20 March 2020.


def move_zeros(array):

    zeros = 0
    new_array = []
    for i in array:
        if i is False:
            new_array.append(False)
        elif i == 0 or i == 0.0:
            zeros += 1
        else:
            new_array.append(i)
    zeros_array = [0 for i in range(zeros)]
    return new_array + zeros_array
