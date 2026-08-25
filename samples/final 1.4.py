def second_largest(nums):
    largest =second= -1
    for num in nums:
        if num > largest:
            second =largest
            largest=num
        elif num>second and num != 0:
            second =num
    return second
print(second_largest([5,5,6,7,8,9]))