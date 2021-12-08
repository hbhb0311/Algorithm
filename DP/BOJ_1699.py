import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i

    for j in range(2, i):
        if j*j > i:
            break

        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[n])

