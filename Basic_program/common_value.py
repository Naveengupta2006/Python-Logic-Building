list1 = [1,2,3,4,5,6]
list2 = [3,4,5,6,7,8]

common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print(common)             