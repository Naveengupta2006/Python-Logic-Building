class parent:
    def __init__(self):
        self.__num = 100
    
    def show(self):
        print("parent:",self.__num)

class child(parent):
    def __init__(self):
        super().__var()
        self.__var=10

    def show(self):
        print("child",self.__var)

obj = child()
obj.show()
