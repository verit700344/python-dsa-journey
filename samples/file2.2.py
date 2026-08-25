def min_subarray_length(target,nums):
    left =0
    cur_sum=0
    min_len=float('inf')

    for right in range (len(nums)):
        cur_sum+=nums[right]
    
        while cur_sum >= target:
            min_len=min(min_len,right-left+1)
            cur_sum-=nums[left]
    return 0 if min_len ==float('inf') else min_len
print(min_subarray_length( 7,[7,6,7,7,88]))

