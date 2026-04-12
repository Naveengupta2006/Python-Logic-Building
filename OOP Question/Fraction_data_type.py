class Fraction:
    # parameterized constructor

    def __init__(self,x,y):
          self.num = x
          self.den = y

    def __str__(self):  # automatic excute the str code.
        return '{}/{}'.format(self.num, self.den) # use the formating string to show the exact fromat.
    
    def __add__(self, other): # this method work only for addition to fraction.
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)
    
    def __sub__(self, other): # this method work onlty for subtraction to fraction.
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)
    
    def __mul__(self, other): # this method work onlty for Multiplication to fraction.
        new_num = self.num*other.num
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)
    
    def __truediv__(self, other): # # this method work onlty for divide to fraction. 
        new_num = self.num*other.den
        new_den = self.den*other.num

        return '{}/{}'.format(new_num, new_den)

    def convert_to_deciaml(self):
        return self.num/self.den    
         
         
fr1 = Fraction(3,4)
fr2 = Fraction(1,2)

'''print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)'''

print(fr1.convert_to_deciaml())