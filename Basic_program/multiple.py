def multiple_by_3_or_7(num):
    if num % 3 == 0 or num % 7 == 0:
        return "The number is multiple by 3 or 7"
    else:
        return "The number is not multiple by 3 or 7"
    

print(multiple_by_3_or_7(20))    