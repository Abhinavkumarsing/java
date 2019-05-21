class BMW:
    def __init__(self,model,year,make):
        self.model=model
        self.year=year
        self.make=make
    def start(self):
        print("Start thr Car")
    def stop(self):
        print("stoping the car")
class threeseries(BMW):
    def __init__(self,cruseContrelEnable,model,year,make):
        BMW.__init__(self,model,year,make)
        self.cruseContrelEnable=cruseContrelEnable
    def ready(self):
        print("lets go")
class fiveseries(BMW):
    def __init__(self,parkingAssistEnabled,model,year,make):
        BMW.__init__(self,model,year,make)
        self.parkingAssistEnabled=parkingAssistEnabled
threeseries=threeseries(True,"abc",2019,"defg")
print(threeseries.cruseContrelEnable)
print(threeseries.model)
print(threeseries.year)
print(threeseries.make)

fiveseries=fiveseries(False,2019,"gh67" ,'chapla')
print(fiveseries.parkingAssistEnabled)
print(fiveseries.model)
print(fiveseries.year)
print(fiveseries.make)
threeseries.start()
threeseries.stop()
threeseries.ready()