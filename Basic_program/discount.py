amount = int(input('Enter a number: '))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

final = amount - discount

print('Original Amount =',amount)
print('Discount =',discount)
print('Final pay Amount =',final)