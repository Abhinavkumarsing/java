#polymorphism is used for those data which is used for different type of work with the same name
class Duck:
    def talk(self):
        print("quack quack")
class Human:
    def talk(self):
        print("hello")

def callTalk(obj):
    obj.talk()

d=Duck()
callTalk(d)

h=Human()
callTalk(h)