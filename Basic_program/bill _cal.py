'''Electricity bill calculation based on units:

≤100 → ₹1/unit

≤200 → ₹2/unit

200 → ₹5/unit'''

units = int(input('Enter a Units: '))

if units <= 100:
    bill = units * 100
elif units <= 200:
    bill = (100 * 1) + (units - 100) * 2
else:
    bill = (100 * 1) + (100 * 2) + (units - 200) * 5

print("Total Electricity Bill = ",bill)