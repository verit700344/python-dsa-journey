def lucky_path(grid):
    rows,cols=len(grid),len(grid[0])
    dp=[[0]*cols for _ in range(rows)]

    if grid[0][0] == 0:
        return 0
    grid[0][0]=1
    for i in range(rows):
        for j in range(cols):
            if grid [i][j]==1:
                if i>0:
                    dp[i][j]+=dp[i-1][j]
                if j>0:
                    dp[i][j]+=dp[i][j-1]
    return dp[-1][-1]