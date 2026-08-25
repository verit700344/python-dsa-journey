def move_zeros(nums):
    index = 0
    for num in nums:
        if num !=0:
            nums[index]=num
            index+=1
    while index < len(nums):
            nums[index]=0
            index+=1
    return nums
print(move_zeros([0,9,0,7,7,78]))