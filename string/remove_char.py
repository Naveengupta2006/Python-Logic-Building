# Removal of all characters from a string except integers

str1 = input('enter a string: ')

result = ""

for s in str1:
    if s.isdigit():
        result += s

print("original Result:", s)
print("Result:", result)        