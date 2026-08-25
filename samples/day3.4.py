def min_coins(coins,amount):
    coins.sort(reverse=True)
    count=0
    for coin in coins:  
        count+= amount//coin
        amount %= coin
    return count

print(min_coins([1,7,98,8],67))
