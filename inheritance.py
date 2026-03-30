class A:
    def __init__(self):
        self.x=10
    def getx(self):
        print("AX is ",self.x)
    
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20
        
    def gety(self):
        print("BY is ",self.y)
        
obj1=B()
obj1.gety()
obj1.getx()

        