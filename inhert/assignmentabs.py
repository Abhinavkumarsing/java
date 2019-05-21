from abc import abstractclassmethod,ABC

class TouchScreenLaptop(ABC):

   

    @abstractclassmethod

    def scroll(self):

        pass

    @abstractclassmethod

    def click(self):

        pass

   

class HP(TouchScreenLaptop):

    def scroll(self):

        print('HP Laptop scroll')

       

class DELL(TouchScreenLaptop):

    def scroll(self):

        print('Dell Laptop scroll')

       

class HPNotebook(TouchScreenLaptop):

        def click(self):

            print('HPNotebook Laptop click')

           

        def scroll(self):

            print('HPNotebook Laptop scroll')

           

class DELLNotebook(TouchScreenLaptop):

        def click(self):

            print('DELLNotebook Laptop click')

           

        def scroll(self):

            print('DELLNotebook Laptop scroll')

           

           

hp=HPNotebook()

hp.click()

hp.scroll()



dell= DELLNotebook()

dell.click()

dell.scroll()