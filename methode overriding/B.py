from A import A
class B(A) :
    def __init__(self):
        super().__init__()
        self.x=20
    def getx(self):
        super().getx()
        print("B X is ",self.x)
