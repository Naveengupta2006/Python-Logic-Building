# Removal of all characters from a string except integers

str1 = input('enter a str: ')

result = ""

for c in str1:
    if c.isdigit():
        result += c

print("Original String",str1)
print('Result', result)        