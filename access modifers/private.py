class A :
    def __init__(self):
        self.__name="Ara"
    def display(self):
        print("My name is",self.__name)

class B(A):
    def dis2(self):
        print("B Name is ",self.__name)
obj1= B()
obj1.dis2()    