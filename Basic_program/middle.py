a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

if (a > b and a < c) or (a > c and a < b):
    middle = a
elif (b > a and b < c) or (b > c and b < a):
    middle = b
else:
    middle = c

print('middle is ', middle)