def laske_keskiarvo(numerot: list) -> float:
    """
    Laskee keskiarvon annetuista numeroista.

    >>> laske_keskiarvo([42])
    42.0

    >>> laske_keskiarvo([1, 2])
    1.5

    >>> laske_keskiarvo([1, 2, 3, 4, 5, 6])
    3.5

    >>> laske_keskiarvo([])
    0
    """

    if len(numerot) == 0:  # "guard clause"
        return 0

    summa = 0
    for numero in numerot:
        summa += numero

    return summa / len(numerot)
