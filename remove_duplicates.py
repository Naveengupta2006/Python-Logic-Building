num = [1,2,2,3,1,2,4,1,5]

unique = []
for n in num:
    if n not in unique:
        unique.append(n)

print(unique)        