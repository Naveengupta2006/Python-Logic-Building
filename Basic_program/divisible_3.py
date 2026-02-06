# Check whether a number is divisible by 4 but not by 8.

num = int(input('Enter a number: '))

if num % 4 == 0 and num % 8 != 0:
    print('Divisible By 4')
else:
    print('condition not satisfied')