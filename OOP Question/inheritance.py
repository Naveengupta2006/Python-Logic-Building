class parent:

    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class child(parent):

    def __init__(self,val,num):
        self.__val = val

    def get_val(self):
        return self.__val

son = child(100,10)
print("Parent: Num:", son.get_num())
print("Child: val: ", son.get_val())         

# the answer is error