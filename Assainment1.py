class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def set_marks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def calctotal(self):
        return self.m1+self.m2+self.m3
    def average (self):
        return self.calctotal()/3
    def grade (self):
        ava=self.average()
        if ava>=75 and ava<100 :
            return "A"
        elif ava>=65 and ava<75 :
            return "B"
        elif ava>=55 and ava<65 :
            return "C"
        else :
            return "F"
    def display(self):
        print ("Student Name is "+self.name)
        print ("Student id is ",self.id)
        print ("Student Marks 1 is ",self.m1)
        print ("Student Marks 2 is ",self.m2)
        print ("Student Marks 3 is ",self.m3)
        print("Student total is ",self.calctotal())
        print("Student average is ",self.average())
        print("Student grade is "+self.grade())
        
stu1=Student(1000,"Ara")
stu1.set_marks(89,85,90)
stu1.display()
        
        
        
        
        
        
        
        