class NewClass1:
    def __init__(self):
        self.attribute1 = "NewClass1 attribute"

    def method1(self):
        print("NewClass1 method")


class NewClass2:
    def __init__(self):
        self.attribute2 = "NewClass2 attribute"

    def method2(self):
        print("NewClass2 method")


class SecondClass(NewClass1, NewClass2):
    def __init__(self):
        NewClass1.__init__(self)
        NewClass2.__init__(self)
        self.attribute3 = "SecondClass attribute"

    def method3(self):
        print("SecondClass method")




instance = SecondClass()


print(instance.attribute1)
instance.method1()


print(instance.attribute2)
instance.method2()


print(instance.attribute3)
instance.method3()