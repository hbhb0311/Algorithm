def diffusion():
    global graph_c
    graph_c = deepcopy(graph)
    for r in range(R):
        for c in range(C):
            if graph[r][c] != 0 and graph[r][c] != -1:
                cnt = 0
                for d in D:
                    x = c + d[1]
                    y = r + d[0]
                    if 0 <= y < R and 0 <= x < C and graph[y][x] != -1:
                        graph_c[y][x] += graph[r][c] // 5
                        cnt += 1
                graph_c[r][c] -= (graph[r][c] // 5) * cnt
    return graph_c

def power(x, y, dir):
    temp = deepcopy(graph_c)
    graph_c[x][y] = 0
    cx, cy = x, y - 1

    for i in range(4):
        while True:
            nx = x + D[dir[i]][0]
            ny = y + D[dir[i]][1]

            if nx == cx and ny == cy:
                return
            if 0 <= nx < R and 0 <= ny < C:
                graph_c[nx][ny] = temp[x][y]
            else:
                break
            x, y = nx, ny

import sys
from copy import deepcopy

input = sys.stdin.readline
R, C, T = map(int, input().split())
graph = []
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
air_idx = 0
for i in range(R):
    val = list(map(int, input().split()))
    graph.append(val)
    if -1 in val:
        air_idx = i

for _ in range(T):
    updated = diffusion()
    power(air_idx, 1, [2, 0, 3, 1])
    power(air_idx - 1, 1, [2, 1, 3, 0])
    graph = deepcopy(graph_c)

answer = 0
for lst in graph:
    answer += sum(lst)
print(answer + 2)