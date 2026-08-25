def coin_change(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for coin in coins:  
        for i in range(coin,amount + 1):
            dp[i]=min(dp[i],dp[i-coin])

    return dp[amount] if dp[amount] !=float('inf') else -1

print(coin_change([1,5,6],7))


