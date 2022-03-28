import sys
from collections import deque

def bfs():
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i == 0:
                continue

            if i not in visited:
                queue.append(i)
                visited.append(i)


input = sys.stdin.readline

n = int(input())
pair = int(input())
graph = [[0] for _ in range(n + 1)]

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [1]
bfs()
print(len(visited) - 1)
