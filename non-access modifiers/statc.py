class student:
    stu_name="Ara"
    @classmethod
    def printn(cls):
        cls.stu_name="kumar"
        print("Student Name: ",cls.stu_name)
    @staticmethod
    def printstu():
  
        print("Student Name: ",student.stu_name)
    
        
        
        
stu1= student()

stu1.printstu()
stu1.printn()
print(student.stu_name)