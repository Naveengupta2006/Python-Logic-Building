def count_even_odd(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even number is : ", even)
    print("odd number is :", odd)


nums = [1,2,3,4,5,6,7,8]
count_even_odd(nums)                