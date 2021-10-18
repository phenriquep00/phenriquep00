from packex110 import ex110


def sumary(c):
    suma = {'half': ex110.half(c, co=True),
            'double': ex110.double(c, co=True),
            'increase': ex110.increase(c, 80, co=True),
            'decrease': ex110.decrease(c, 35, co=True)}

    print('-' * 30)
    print('         PRICE SUMARY')
    print('-' * 30)

    for i, v in suma.items():
        print(f'{i:<15}', end='')
        print(f'{v:<15}')
    print()
