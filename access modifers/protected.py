class A :
    def __init__(self):
        self._name="Ara"
    def display(self):
        print("My name is",self._name)

class B(A):
    def dis2(self):
        print("B Name is ",self._name)
obj1= B()
obj1.dis2()    
print(obj1._name)