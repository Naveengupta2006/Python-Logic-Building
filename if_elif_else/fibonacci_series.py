'''
Display Fibonacci series up to 10 terms.
Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34

'''

# start with first two number
first = 0
second = 1
# print first two terms
print(first, end= " ")
print(second, end= " ")
# use a loop
for i in range(8):
    next_num = first + second
    print(next_num, end= " ")
    # update version
    first = second 
    second = next_num