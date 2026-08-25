def lis(nums):
    if not nums:
        return 
    dp=[1]*len(nums)
    for i in range(1,len(nums)):
        for j in range (i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print(lis([10,2,2,2,3,6,66]))
