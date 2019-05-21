class Student:
    major="cse"
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
s1=Student(1,'john')
s2=Student(3,"Rohan")
print (s1.major)
print(s1.name)
print(s2.rollno)
