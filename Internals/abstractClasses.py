import abc as x


class mainCaculation(x.ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @x.abstractmethod
    def calculate(self):
        pass


class Addition(mainCaculation):
    def calculate(self):
        sum = []
        for i in range(0, len(self.a)):
            sum.append(self.a[i] + self.b[i])
        print("Sum is : ", sum)


class Subtraction(mainCaculation):
    def calculate(self):
        sub = []
        for i in range(0, len(self.a)):
            sub.append(self.b[i] - self.a[i])
        print("Subtracted value is : ", sub)


class Multiplication(mainCaculation):
    def calculate(self):
        mul = []
        for i in range(0, len(self.a)):
            mul.append(self.a[i] * self.b[i])
        print("Product is : ", mul)


class Division(mainCaculation):
    def calculate(self):
        div = []
        for i in range(0, len(self.a)):
            div.append(self.a[i] // self.b[i])
        print("Product is : ", div)


a = []
b = []

n = int(input("Enter the n value: "))

print("Enter first list: ")
for i in range(0, n):
    a.append(int(input()))

print("Enter the second list: ")
for i in range(0, n):
    b.append(int(input()))

while True:
    print("1. Add\n2. Sub\n3. Multiply\n4. Division\n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        Addition(a, b).calculate()
    elif ch == 2:
        Subtraction(a, b).calculate()
    elif ch == 3:
        Multiplication(a, b).calculate()
    elif ch == 4:
        Division(a, b).calculate()
    elif ch == 5:
        break
    else:
        print("Invalid choice ")
        break
