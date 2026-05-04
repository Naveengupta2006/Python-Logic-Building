class phone:

    def __init__(self, price, brand, camera):
        print("Inside phone construtor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class smartphone(phone):
    def buy(self):
        print("buying a smartphone")

s = smartphone(20000, "apple", 13)        
s.buy()