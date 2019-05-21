class Student:
    def __init__(self):
        self.__id=123
        self.__name='Abhinav'
    
    def display(self):
        print(self.__id)
        print(self.__name)

s=Student()
s.display()  #Display value in Encapsulation
print(s._Student__id)  #we can Access the private field using through that function
print(s._Student__name)