a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

if a == b == c:
    print('Equilateral Angle')
elif a == b or b == c or a == c:
    print('Isosceles Angle')
else:
    print('Scalene Angle')        
