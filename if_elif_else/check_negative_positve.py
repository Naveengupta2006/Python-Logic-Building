def positive_negative_zero(num):
    if num > 0:
        return "Postive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
print(positive_negative_zero(0))