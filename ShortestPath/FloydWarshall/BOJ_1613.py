# 블로그 참고해서 업그레이드

n, k = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][i] and graph[i][b]:
                graph[a][b] = 1

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())

    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    else:
        print(0)