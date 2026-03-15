# Write a function that counts the number of elements in a list.

def count_ele(number):
    count = 0
    for i in number:
        count += 1
    return count

print(count_ele([1,2,3,4]))    