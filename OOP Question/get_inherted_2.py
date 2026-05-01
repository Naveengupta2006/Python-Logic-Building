# construtor example 2

class phone:
    def __init__(self, price, brand, camera):  # not excute this code why: because child class axis is own construtor. so parent class not excute.
        print('Inside phone construtor')
        self.__price = price # price is private
        self.brand = brand
        self.camera = camera


class smartphone(phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print('inside smartphone construtor')


s = smartphone("android",2)

