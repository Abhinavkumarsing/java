'''class Student:
    def setId(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setName(self,Name):
        self.Name=Name
    def getName(self):
        return self.Name
s=Student()
s.setId(123)
s.setName('Abhinav')
print(s.getid())
print(s.getName())'''
class Patient:

    def __init__(self):

        self.__id = None

        self.__name = None

        self.__ssc = None

    def setname(self,name):

        self.__name = name

    def setid(self,ids):

        self.__id = ids

    def setssc(self,ssc):

        self.__ssc = ssc

    def getname(self):

        return self.__name

    def getid(self):

        return self.__id

    def getssc(self):

        return self.__ssc

       

p1 = Patient()

p1.setname("name")

print(p1.getname())

