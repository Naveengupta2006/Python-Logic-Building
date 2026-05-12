class phone:
    def __init__(self, price, brand, camera):
        print("Inside phone construtor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

class smartphone(phone):
    pass

class feature(phone):
    pass

smartphone(1000,"apple","13px").buy()
