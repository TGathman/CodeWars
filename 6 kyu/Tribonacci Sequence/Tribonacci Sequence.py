# Python 3.8, 20 March 2020


def tribonacci(signature, n):

    if n <= 3:
        return signature[0:n]

    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature
