num = int(input('enter a decimal number'))

original = num
remainders = []

if num == 0:
    print('Binary')
else:
    while num > 0:
        remainder = num % 2
        remainders.append(remainder)
        num = num // 2

    remainders.reverse()

    binary = "".join(map(str, remainders))

print('original', original)
print('binary', binary)        



