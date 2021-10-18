from venv.ex115.modules import color


def write_title(txt):
    length = len(txt)

    def lining():
        print(color.magenta('_') * 30, end='')
        for e in range(0, length):
            print(color.magenta('_'), end='')
        print()

    lining()
    print(color.magenta(f'               {txt:^}'))
    lining()


def line():
    print(color.magenta('_' * 39))
