# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

# take user input 
a = int(input('enter a angle:'))
b = int(input('enter a anglr:'))
c = int(input('enter a angle:'))

# check triangle or not.
if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print('triangle')
else:
    print('not triangle')    