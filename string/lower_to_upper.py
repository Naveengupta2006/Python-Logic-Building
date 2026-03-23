s = "hfynMJDMDNndhfhfNFFJ"

lowercase = [c for c in s if c.islower()]
uppercase = [c for c in s if c.isupper()]

result = "".join(lowercase + uppercase)

print("original ",s)
print("Result", result)