# Python 3.8, 20 March 2020.


def nb_year(p0, percent, aug, p, year=0):

    if p0 >= p:
        return year

    pop = p0 * (1 + percent / 100) + aug
    year += 1

    return nb_year(pop, percent, aug, p, year)
