# create the function

'''Write a Python function that takes a list and returns a new list with unique elements of the first list.'''

def get_unique_elements(lst):
    seen = set()
    unique = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique

my_list = [1,2,3,2,3,2]
result = get_unique_elements(my_list)
print(result)