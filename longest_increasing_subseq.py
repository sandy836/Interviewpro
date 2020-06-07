def longestIncreasingSubseq(arr):
    if not arr:
        return 0
    _max_len = 1
    dp = [1]*len(arr)
    for i in range(0, len(arr)):
        for j in range(0, i):
            if arr[i]>arr[j] and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
                _max_len = max(_max_len, dp[i])
    return _max_len
    
print(longestIncreasingSubseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))