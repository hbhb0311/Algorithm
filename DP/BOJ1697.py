import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * 100001

if n <= k:
    for i in range(len(dp)):
        if i < n:
            dp[i] = n - i
        else:
            dp[i] = i - n

    for i in range(1, len(dp) - 1):
        dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1)

        if i <= 50000:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
else:
    dp[k] = n - k

print(dp[k])