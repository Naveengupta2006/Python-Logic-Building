# Create a function that checks whether a number is even or odd.

def count_even_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    

check = int(input('enter a number'))
print(count_even_odd(check))