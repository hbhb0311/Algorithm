import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    dp_sub = []

    for j in range(i):
        if arr[i] > arr[j]:
            dp_sub.append(dp[j])

    try:
        dp[i] += max(dp_sub)
    except:
        continue

print(max(dp))