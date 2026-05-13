class phone:  # single parent
    def __init__(self, price, brand, camera):
        print("Inside phone construtor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

class smartphone(phone): # child 1
    pass

class featurephone(phone): # child 2
    pass

smartphone(1000,"apple","13px").buy()
featurephone(1000,"lava","1px").buy()
