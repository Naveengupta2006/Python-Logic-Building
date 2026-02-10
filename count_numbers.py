'''
Write a function that:

1. Takes a list of intergers.
2. Returns the count of numbers greater than 50.

Do not use built in- functions like filter().
'''

def count_greater_50(numbers):
    count = 0
    for num in numbers:
        if num > 50:
            count += 1

    return count

num = [10,60,45,80,30]
result = count_greater_50(num)
print(result)        