def lcs(t1, t2):
    m,n=len(t1),len(t2)
    dp=[[0]*(n+1)for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if t1[i-1]==t2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[j][i-1])
    return dp[m][n]
print(lcs("AHFJGJ","SDFFAS"))


