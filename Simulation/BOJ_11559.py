import sys
from collections import deque
input = sys.stdin.readline


def cntCheck(x, y):
    need = deque()
    visited = []
    need.append((x, y))

    while need:
        node = need.popleft()
        if node not in visited:
            visited.append(node)
            for i in range(4):
                nx = node[0] + d[i][0]
                ny = node[1] + d[i][1]
                if 0 <= nx < 12 and 0 <= ny < 6 and graph[node[0]][node[1]] == graph[nx][ny]:
                    need.append((nx, ny))
    return visited


def fall():
    for i in range(11, 0, -1):
        for j in range(6):
            if graph[i][j] == '.':
                for k in range(i - 1, -1, -1):
                    if graph[k][j] != '.':
                        graph[i][j] = graph[k][j]
                        graph[k][j] = '.'
                        break


graph = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
total_cnt = 0
cnt = 1

for _ in range(12):
    graph.append(list(input().rstrip()))

while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                visit = cntCheck(i, j)
                if len(visit) >= 4:
                    flag = True
                    cnt += 1
                    for v in visit:
                        graph[v[0]][v[1]] = '.'
    if flag == True:
        total_cnt += 1
        fall()
    else:
        break
print(total_cnt)