from abc import abstractclassmethod,ABC
class TouchscreenLaptop(ABC):
    @abstractclassmethod
    def scroll(self):
        pass

    @abstractclassmethod
    def click(self):
        pass

class HP (TouchscreenLaptop):
    def scroll(self):
        print("hp LaptopScrolled")

class Dell (TouchscreenLaptop):
    def scroll(self):
        print("Dell Laptop is Scrolled")

class HpNoteBook(TouchscreenLaptop):
    def click(self):
        print("HpNoteBook Is Clickable")

class DellNoteBook(TouchscreenLaptop):
    def click(self):
        print("DellnoteBook is CliCable")
        
hp=HpNoteBook()
hp.click()

dp=DellNoteBook()
dp.click()