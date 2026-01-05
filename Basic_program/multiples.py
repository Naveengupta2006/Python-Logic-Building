def multiple_by_3_or_7(num):
    if num % 3 == 0 or num % 7 == 0:
        return 'The Number is Multiple by 3 or 7'
    else:
        return 'The Number is not Multiple by 3 or 7'
    
number = int(input("Enter a Number: "))
result = multiple_by_3_or_7(number)
print(result)
