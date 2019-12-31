import abc as x


class MainCalculation(x.ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @x.abstractmethod
    def calculate(self):
        pass


class Addition(MainCalculation):
    def calculate(self):
        sum = []
        for i in range(0, len(self.a)):
            sum.append(self.a[i] + self.b[i])
        print("Sum is ", sum)


a = []
b = []

n = int(input("Enter the n value: "))

print("List 1: ")
for i in range(0, n):
    a.append(int(input()))

print("List 2: ")
for i in range(0, n):
    b.append(int(input()))

Addition(a, b).calculate()
