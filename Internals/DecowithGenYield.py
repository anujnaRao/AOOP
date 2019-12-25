import time


def deco_time(func):
    start = time.time()
    print("Start: ", start)
    func()
    end = time.time()
    print("End: ", end)
    diff = end - start
    print("Difference: ", diff)
    return func


def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


@deco_time
def execute():
    fib = fibonacci()
    n = int(input("N value: \n"))
    for i in range(n):
        print(next(fib))


#execute()
