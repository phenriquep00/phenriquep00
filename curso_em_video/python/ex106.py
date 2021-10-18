
# functions:
def ihelp(a):
    from time import sleep

    def write(txt):
        length = len(txt)

        def lining():
            print(f'\033[1;30;44m~' * 4, end='')
            for e in range(0, length):
                print('~', end='')
            print()

        lining()
        print(f'  {txt:^}')
        lining()

    write(f'Looking for the doc of the {a} function...')

    sleep(.7)
    help(a)


# main
while True:
    method = str(input('function name --> ')).lower()
    ihelp(method)
    ask = str(input('\033[0;30;42mWant help with another function? [y/n] ').lower()[0])
    print(f'\033[m')
    if 'n' in ask:
        print(f'\033[1;31;40mBYE!')
        break
