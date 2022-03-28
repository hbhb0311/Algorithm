import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
jew = []
bag = []

for _ in range(n):
    jew.append(list(map(int, input().split())))

for _ in range(k):
    bag.append(int(input()))

jew.sort()
bag.sort()

result = []
ans = 0
for b in bag:
    while jew and b >= jew[0][0]:
        heapq.heappush(result, -jew[0][1])
        heapq.heappop(jew)

    if result:
        ans += heapq.heappop(result)
    elif not jew:
        break
print(-ans)