def staircase(n):
    if n==1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]

print(staircase(4))
print(staircase(5))