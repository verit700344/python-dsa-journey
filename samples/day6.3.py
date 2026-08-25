def rob_houses(num):
    if not num:
        return 0
    if len(num)==1:
        return num[0]

    dp=[0]*(len(num)+1)
    dp[0]=num[0]
    dp[1]=max(num[1],num[0])

    for i in range (2,len(num)):
        dp[i]=max(dp[i-1]+dp[i-2],dp[i-1])
    return dp[-1]
print(rob_houses([2,7,9,3,1]))  # Output: 12    
   