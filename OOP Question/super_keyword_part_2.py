class phone:

    def __init__(self, price, brand, camera):
        print("Inside phone construtor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
class smartphone(phone):

    def __init__(self, price, brand , camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone construtor")

s = smartphone(20000, "samsung", 12, "android", 2)

print(s.os)
print(s.brand)