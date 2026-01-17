nums = [2,4,3,5,7,8,9]
traget = 10

seen = set()
for num in nums:
    needed = traget - num
    if needed in seen:
        print(needed, num)
        seen.add(num)