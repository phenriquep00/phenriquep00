def coin(c):
    return f'R${c:.2f}'


def half(n, co=False):
    if co:
        n = n / 2
        return coin(n)
    else:
        return n / 2


def double(n, co=False):
    if co:
        n = n * 2
        return coin(n)
    else:
        return n * 2


def increase(n, r=0, co=False):
    if co:
        n = n + (n * (r / 100))
        return coin(n)
    else:
        return n + (n * (r / 100))


def decrease(n, r=0, co=False):
    if co:
        n = n - (n * (r / 100))
        return coin(n)
    else:
        return n - (n * (r / 100))
