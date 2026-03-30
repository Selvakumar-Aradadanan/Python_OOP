from B import B 
from A import A
class C(B,A):
    def __init__(self):
        super().__init__()
        self.z=30
    def getz(self):
        print("C Z is ",self.z)