class A:
    def __init__(self,x):
        self.x=x
    def getx(self):
        print("AX is ",self.x)
    
class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
        
    def gety(self):
        print("BY is ",self.y)
        
obj1=B(20,10)
obj1.gety()
obj1.getx()

        