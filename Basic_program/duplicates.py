# How do you find duplicates elements in a list without using built in function?
nums = [1,2,2,3,3,3,4]
duplicates = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            if nums[i] not in duplicates:
                duplicates.append(nums[i])
print(duplicates)               