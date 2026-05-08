class parent:
    def __init__(self):
        self.num = 100

class child(parent):

    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.num)
        print(self.var)

son=child()
son.show()        