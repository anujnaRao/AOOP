class MyClass(type):
    def __new__(cls, name, base, dict):
        print(cls)
        print(name)
        print(base)
        print(dict)
        return super(MyClass, cls).__new__(cls, name, base, dict)

    def __init__(cls, name, base, dict):
        print(cls)
        print(name)
        print(base)
        print(dict)
        super(MyClass, cls).__init__(name, base, dict)


class SubClass(metaclass=MyClass):
    def display(self, arg):
        print("Argument: ", arg)

    val = 10
    str = 'HI'


s = SubClass()
s.display("RV")
