class Student :
   def __init__(self,fname,id,lname):
       self.fname=fname
       self.id=id
       self.lname=lname
   def getfull_name (self):
       return self.fname+" "+self.lname
   def display(self):
       print("My name is "+self.fname)
       print("My id is "+str(self.id))
       print ("My full name is "+self.getfull_name())


stu1=Student("Ara",1000,"Selva")
stu1.display()
stu2=Student("Aru",2000,"Selva")
stu2.display()