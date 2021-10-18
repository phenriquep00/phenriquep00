import color


def read_int(txt):
    global number
    while True:
        try:
            number = int(input(txt))
        except (TypeError, ValueError):
            print(color.red('ERROR: Please type a valid integer number!'))
            continue
        except KeyboardInterrupt:
            print(color.yellow('\nRun interrupted by user!'))
            return 0
        if isinstance(number, int):
            return number
            break


def read_float(txt):
    global number
    while True:
        try:
            number = float(input(txt))
        except (TypeError, ValueError):
            print(color.red('ERROR: Please type a valid float number!'))
            continue
        except KeyboardInterrupt:
            print(color.yellow('\nRun interrupted by user!'))
            break
        if isinstance(number, float):
            return number
            break


number = ''
int_num = read_int('Type a integer number: ')
float_num = read_float('Type a float number: ')
print(color.green(f'You typed the integer number {int_num} and the float number {float_num}'))
