# Append second string in the middle of first string

str1 = input('enter a string: ')
str2 = input('enter a string: ')

mid = len(str1) // 2

left = str1[:mid]
right = str2[mid:]

result = left + str2 + right

print("result", result)