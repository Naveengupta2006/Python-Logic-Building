# Replace all negative values with 0 in a list/array.
nums = [3,-1,5,-7,2,-4]

for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0

print(nums)