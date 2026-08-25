def max_sum_subarray(nums,k):
    window_sum = sum(nums[ :k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum+= nums [i] - nums [i-k]
        max_sum = max(window_sum,max_sum)
    return max_sum
print(max_sum_subarray([4,5,6,7,7],7))