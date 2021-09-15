import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]] * n

for i in range(1, n):
    if dp[i - 1] < 0:
        dp[i] = arr[i]
    else:
        dp[i] = dp[i - 1] + arr[i]
print(max(dp))