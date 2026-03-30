class Student1:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print("my name is"+self.name)
        print("my id is"+str(self.id))


stu1=Student1("seelan",20)
stu1.display()