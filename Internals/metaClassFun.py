class MyClass(type):
    def __new__(cls, name, bases, dic):
        print(cls)
        print(name)
        print(bases)
        print(dic)
        return super(MyClass, cls).__new__(cls, name, bases, dic)

    def __init__(self, name, bases, dic):
        print(self)
        print(name)
        print(bases)
        print(dic)
        super(MyClass, self).__init__(name, bases, dic)


class SubClass(metaclass=MyClass):
    def display(self, arg):
        print("Argument is: ", arg)

    b = 10


ar = SubClass()
ar.display("HI")
