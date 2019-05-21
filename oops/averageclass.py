class Bca:
    def __init__(self,subject,ratings):
        self.subject=subject
        self.ratings=ratings
    
    def average(self):
        noOfRatings= len(self.ratings)
        average=sum(self.ratings)/noOfRatings
        print("average of the num",self.subject "is",average)
    
c1= Bca("python",[4,5,5,5,5])
print(c1.subject)
print(c1.ratings)
c1.average()
    
c2= Bca("Dbms",[4,1,4,2,3])
print(c2.subject)
print(c2.ratings)
c2.average()
