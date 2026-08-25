def max_sum_subarray(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum

    for i in range(k,len(arr)):
        window_sum+=arr[i],arr[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum
print(max_sum_subarray([1,3,5,6,7],5))
