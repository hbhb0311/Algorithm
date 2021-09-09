import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = 0
i, j = 0, 1

while j <= len(dist):
    if cost[i] > cost[j]:
        ans += cost[i] * dist[j - 1]
        i = j
        j = i + 1
    else:
        ans += cost[i] * dist[j - 1]
        j += 1
print(ans)