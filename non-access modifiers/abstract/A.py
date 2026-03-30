class A:
    from abc import ABC ,abstractmethod 
    
    def Turn_left(self):
        pass
    
class B (A):
    def __init__(self):
        super().__init__()
    
    def Turn_left(self):
        print("Turn the weels left by 90 degrees")
        
        
car1 = B()
car1.Turn_left()