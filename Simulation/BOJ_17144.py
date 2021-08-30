def upper_rotate(idx):
    for i in range(idx - 1, 0, -1):
        graph_c[i][0] = graph_c[i - 1][0]
    for i in range(C - 1):
        graph_c[0][i] = graph_c[0][i + 1]
    for i in range(idx):
        graph_c[i][-1] = graph_c[i + 1][-1]
    for i in range(C - 1, 1, -1):
        graph_c[idx][i] = graph_c[idx][i - 1]
    graph_c[idx][1] = 0

def lower_rotate(idx):
    for i in range(idx + 1, R - 1):
        graph_c[i][0] = graph_c[i + 1][0]
    for i in range(C - 1):
        graph_c[-1][i] = graph_c[-1][i + 1]
    for i in range(R - 1, idx, -1):
        graph_c[i][-1] = graph_c[i - 1][-1]
    for i in range(C - 1, 1, -1):
        graph_c[idx][i] = graph_c[idx][i - 1]
    graph_c[idx][1] = 0

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

graph_c = deepcopy(graph)
for _ in range(T):
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
    upper_rotate(air_idx - 1)
    lower_rotate(air_idx)
    graph = deepcopy(graph_c)

answer = 0
for lst in graph:
    answer += sum(lst)
print(answer + 2)