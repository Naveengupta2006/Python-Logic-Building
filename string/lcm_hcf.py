a = int(input('enter a number: '))
b = int(input('enter a number: '))

x = a
y = b

while b != 0:
    temp = b
    b = a % b
    a = temp

HCF = a

# find lcm
lcm = (x * y) // HCF


print('HCF =', HCF)
print('LCM =',lcm)