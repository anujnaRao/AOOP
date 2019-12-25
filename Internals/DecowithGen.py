import time


def deco_time(func):
    start = time.time()
    print("Start time is: ", start)
    func()
    end = time.time()
    print("End time is: ", end)
    diff = end - start
    print("Time take is: ", diff)
    return func


class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


@deco_time
def execute():
    fib = Fibonacci()
    n = int(input("Enter the value n: \n"))
    for i in range(n - 1):
        next(fib)
    print("Fibonacci value: ")
    print(next(fib))
