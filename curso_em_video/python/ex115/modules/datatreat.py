from venv.ex115.modules import color


def read_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(color.red('ERROR: Please type a valid number!'))
            continue
        if isinstance(n, int):
            return n
            break
