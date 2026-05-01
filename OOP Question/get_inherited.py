# constructor example 1

class phone: # this is parent
    def __init__(self, price, brand, camera):
        print("Inside phone construtor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class smartphone(phone): # and this child class
    pass

s = smartphone(20000, 'apple', 13)
s.buy()