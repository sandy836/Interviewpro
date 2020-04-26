def num_ways(n, m):
    dp = [[0]*n for _ in range(m)]
    for i in range(n):
        dp[0][i] = 1
    for j in range(m):
        dp[j][0] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
    return dp[-1][-1]


print(num_ways(3,7))