def max_subarray(num):
    max_sum=cur_sum= num[0]
    for i in range(1,len(num)):
        cur_sum=max(num[i],cur_sum+num[i])
        max_sum=max(max_sum,cur_sum)
    return max_sum
print(max_subarray([1,2,-2,8]))