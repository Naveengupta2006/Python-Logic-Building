a = 12
b = 18

max_num = max(a, b)
while True:
    if max_num % a == 0 and max_num % b == 0:
        print('LCM is :', max_num)
        break
    max_num += 1