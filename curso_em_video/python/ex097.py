def write(txt):
    length = len(txt)

    def lining():
        print('~' * 4, end='')
        for e in range(0, length):
            print('~', end='')
        print()

    lining()
    print(f'  {txt:^}')
    lining()


write('')
