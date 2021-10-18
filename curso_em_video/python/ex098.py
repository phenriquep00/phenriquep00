from time import sleep


def count(a, b, c):
    print('-' * 30)
    if c == 0:
        c = 1

    if c < 0:
        c *= -1
        d = a
        a = b
        b = d
    if a <= b:
        while a <= b:
            print(a, end=' ')
            sleep(.4)
            a += c
        print()
    elif a >= b:
        while b <= a:
            print(a, end=' ')
            sleep(.4)
            a -= c
        print()


count(1, 10, 1)
count(10, 0, 2)
count(a=int(input('start: ')),
      b=int(input('end: ')),
      c=int(input('pass: '))
      )
