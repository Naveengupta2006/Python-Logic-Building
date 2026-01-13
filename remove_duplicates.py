num = [1,2,2,3,3,4,5,6]

unique = []
for n in num:
    if n not in unique:
        unique.append(n)
print(unique)       