class Patient:
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,Name):
        self.name=Name
    def getName(self):
        return self.name
    def setSsn(self,Ssn):
        self.ssn=Ssn
    def getSsn(self):
        return self.ssn
p=Patient()
p.setId(101)
p.setName('Rahul')
p.setSsn('new')
print(p.getId())
print(p.getName())
print(p.getSsn())