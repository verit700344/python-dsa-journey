def min_leng_sub(target,arr):
    left=0
    current_sum=0
    min_len=float('inf')

    for right in range(len(arr)):
        current_sum+=arr[right]
        while current_sum >= target:
            min_len=min(min_len,right-left+1)
            current_sum-=arr[right]
            left+=1

    return 0 if min_len == float('inf') else min_len
print(min_leng_sub(7,[2,3,1,2,4,3]))