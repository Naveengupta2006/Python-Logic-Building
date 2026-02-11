num = int(input('Enter a number: '))

if -9 <= num <= 9: # single digits
    print('single digits number')
elif -99 <= num <= -10 or 10 <= num <= 99:
    print('two digits number')
else:
    print('multi digit')        