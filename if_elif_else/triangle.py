# Check whether a triangle is valid or not.

a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))

if a + b > c and a + c > b and b + c > a:
    print('valid')
else:
    print('Not valid')    