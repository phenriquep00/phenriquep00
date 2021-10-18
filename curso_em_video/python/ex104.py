def read_int(a):
    while not a.isnumeric():
        a = input('Not a integer, please t again: ')
    return f'{a} is a integer'


# main
n = read_int(input('Type a integer value: '))
print(n)
