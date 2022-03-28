import heapq
import sys

input = sys.stdin.readline
V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

start, end = map(int, input().split())

INF = int(1e9)
distance = [INF] * (V + 1)

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:

    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[0]

        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

print(distance[end])