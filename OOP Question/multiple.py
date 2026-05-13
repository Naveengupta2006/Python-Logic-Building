class phone: # parent 1
    def __init__(self, price, brand, camera):
        print("inside phone construtor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

class product: # parent 2
    def review(self):
        print('Customer review')

class smartphone(phone, product): # child
    pass

s = smartphone(20000,"apple", 12)

s.buy()
s.review()