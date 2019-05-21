class Car:
    def __init__(self,model,made):
        self.model=model
        self.made=made
    class Engine:
        def __init__(self,unino):
            self.unino=unino
        def start(self):
            print("Engine Started")
c=Car("bmw",2017)

e=c.Engine(124)
e.start() 

