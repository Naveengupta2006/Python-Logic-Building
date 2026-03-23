s = "JSUbvduDUbudnchdnhdBCGD"

lowercase = [c for c in s if c.islower()]
uppercase = [c for c in s if c.isupper()]

result = "".join(lowercase + uppercase)

print('Original', s)
print('Result', result)