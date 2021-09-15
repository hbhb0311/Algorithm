INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())

    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][i] + graph[i][b], graph[a][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] >= INF:
            graph[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ')
    print()