def fat(a, show=False):
    f = 1
    if show:
        for c in range(a, 0, -1):
            if c == 1:
                print(f' {c} = ', end='')
                f *= c
            else:
                print(f' {c} x', end='')
                f *= c
        return f
    else:
        for c in range(a, 0, -1):
            f *= c
        return f


# Main
num = fat(8)
print(num)
