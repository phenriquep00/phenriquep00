from time import sleep
import os

def progressBar(total):
    progress_bar = ''
    for _ in range(total):
        for i in range(1, 101):
            if _ == i * total / 100:
                progress_bar += '*'
                sleep(.1)
                os.system('cls')
                print(progress_bar," ",i, '%')
    progress_bar += '*'
    sleep(.1)
    os.system('cls')
    print(progress_bar," ",i, '%')


if __name__ == '__main__':
    print(progressBar(int(input('value: '))))    