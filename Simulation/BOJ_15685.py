import sys
input = sys.stdin.readline

dd = [(0, 1), (-1, 0), (0, -1), (1, 0)]
graph = [[1] * 101 for _ in range(101)]
n = int(input().rstrip())
for _ in range(n):
    x, y, d, g = map(int, input().split())
    dAll = [d]
    for _ in range(g):
        dAll.extend([(i + 1) % 4 for i in dAll[::-1]])

    graph[x][y] = 0
    for i in dAll:
        nx = x + dd[i][1]
        ny = y + dd[i][0]
        graph[nx][ny] = 0
        x, y = nx, ny

cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] + graph[i + 1][j] + graph[i][j + 1] + graph[i + 1][j + 1] == 0:
            cnt += 1
print(cnt)