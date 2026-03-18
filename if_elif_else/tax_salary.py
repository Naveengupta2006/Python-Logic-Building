'''
Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%
'''

# take input 
salary = float(input('Enter a salary '))

# calculation detuction
HRA = salary * 0.10
DA = salary * 0.05
PF = salary * 0.03

# apply the tax slap
if salary < 50000:
    tax = 0
elif salary >= 500000 and salary <= 100000:
    tax = 0.10
elif salary >= 100000 and salary <= 2000000:
    tax = 0.20
else:
    tax = 0.30

tax_amount = salary * tax

# calculate total deduction 
total_deduction = HRA + DA + PF + tax_amount

# final hand salary
in_hand = salary - total_deduction

print('Salary',salary)
print('Total Deduction', total_deduction)
print('In hand salary', in_hand)