'''Salary calculation with bonus:

Salary ≥50,000 → 10% bonus

Salary ≥30,000 → 7% bonus

Else → 5% bonus'''

salary = int(input('Enter a salary: '))

if salary >= 50000:
    bouns = salary * 0.10
elif salary >= 30000:
    bouns = salary * 0.07
else:
    bouns = salary * 0.05

total_salary = salary + bouns

print('Salary',salary)
print('bouns',bouns)
print('total salary',total_salary)
