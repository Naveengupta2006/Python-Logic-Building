num = [1,2,3,5]

n = 5

expected_value = n * (n+1) // 2
actual_value = sum(num)

missing_value = expected_value - actual_value
print('Missing Value: ', missing_value)