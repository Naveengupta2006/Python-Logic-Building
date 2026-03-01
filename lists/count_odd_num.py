list = [1,3,24,5,63,4,66,4,3,3]

count = 0
for num in list:
    if num % 2 != 0:
        count += 1
print('odd number ', count)        