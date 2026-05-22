'''Q-1: Rectangle Class
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.'''

'''

Eg. After making above classes and methods, on executing below code:-

my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
Output:

The length of rectangle is:  3
The width of rectangle is:  4
The perimeter of rectangle is:  14
The area of rectangle is:  12


'''


# write the code .
class rectangle:

    def __init__(self, lenght, width): # this is construtor
        self.lenght = lenght # attributes
        self.width = width # attributes

    def perimeter(self): #   method 
        return 2 * (self.lenght + self.width)
    
    def area(self): # method
        return self.lenght * self.width
    
    def display(self):
        print(f"Lenght:",self.lenght)
        print(f"Width: ",self.width)
        print(f"perimeter: ", self.perimeter())
        print(f"area: ",self.area())

my_rectangle = rectangle(3 ,4)
my_rectangle.display()
