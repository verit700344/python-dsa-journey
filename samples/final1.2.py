def add_two(nums,target):
    seen =set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False
print(add_two([2,6,9,8],9))