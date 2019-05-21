class flight:
    def __init__(self,engine):
        self.engine=engine
        
    def startEngine(self):
        self.engine.start()
        
class Airbus:
    def start(self):
        print("airbus Started")
class Boing:
    def start(self):
        print("boing Engine Started")
ae=Airbus()
f=flight(ae)
f.startEngine()

be=Boing()
f1=flight(be)
f1.startEngine()