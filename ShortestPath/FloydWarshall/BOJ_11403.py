INF = int(1e9)
n = int(input())
graph = []
time = [[INF] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            time[i][j] = 1

for i in range(n):
    for a in range(n):
        for b in range(n):
            time[a][b] = min(time[a][b], time[a][i] + time[i][b])

for i in range(n):
    for j in range(n):
        if time[i][j] == INF:
            time[i][j] = 0
        else:
            time[i][j] = 1

for i in range(n):
    for j in range(n):
        print(time[i][j], end=' ')
    print()