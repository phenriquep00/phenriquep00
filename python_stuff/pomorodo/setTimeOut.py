import threading


def set_timeout(func, sec):
    t = None

    def func_wrapper():
        func()
        t.cancel()
    t = threading.Timer(sec, func_wrapper)
    t.start()


if __name__ == '__main__':
    def hello():
        print("Hello, world!")


    set_timeout(hello, 10)  # This is 0.1s = 100ms
