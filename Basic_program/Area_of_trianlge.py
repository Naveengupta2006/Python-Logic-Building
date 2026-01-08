def area_of_triangle(base, height):
    area = 0.5 * base * height # formula for area of triangle
    return area

b = int(input('Enter a number: '))
h = int(input('Enter a number: '))
print('Area of Triangle: ', area_of_triangle(b, h))