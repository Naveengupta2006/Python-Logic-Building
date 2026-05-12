# multilevel 
class product: # grandparent
    def review(self):
        print("Product customer review")

class phone(product): # parent
    def __init__(self, price, brand, camera):
        print("inside phone construtor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class smartphone(phone):
    pass

s = smartphone(20000, "apple", 13)

s.buy() # this is parent method
s.review() # grandparent method