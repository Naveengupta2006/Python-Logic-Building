class phone:
    def __init__(self, price, brand, camera):
        print("inside phone construtor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)

class smartphone(phone): # child class not the axis private member beacuse of encapsulation.
    def check(self):
        print(self.__price)

s = smartphone(20000, 'apple', 13)
s.check()
