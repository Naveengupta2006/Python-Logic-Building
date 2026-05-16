# method overloading

class shape:

    def area(self, a,b=0):
        if b == 0:
            return 3.14*a*a # area of circle
        else:
            return a*b 

s = shape() # create the s object 

print(s.area(2))
print(s.area(3,4))