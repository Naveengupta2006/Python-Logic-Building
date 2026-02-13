# Use a loop to reverse a number (example: 1234 -> 4321).

num = (input('Enter a number: '))

reversed_num = ''
for i in num:
    reversed_num = i + reversed_num
print(reversed_num)