import sys
from copy import deepcopy
input = sys.stdin.readline

def move(d):
    global graph
    if d == 0: # up
        for c in range(n):
            idx = 0
            for r in range(1, n):
                if graph[r][c]:
                    temp = graph[r][c]
                    graph[r][c] = 0
                    if graph[idx][c] == temp:
                        graph[idx][c] = 2 * temp
                        idx += 1
                    elif graph[idx][c] == 0:
                        graph[idx][c] = temp
                    else:
                        idx += 1
                        graph[idx][c] = temp
    elif d == 1: # down
        for c in range(n):
            idx = n - 1
            for r in range(n - 2, -1, -1):
                if graph[r][c]:
                    temp = graph[r][c]
                    graph[r][c] = 0
                    if graph[idx][c] == temp:
                        graph[idx][c] = 2 * temp
                        idx -= 1
                    elif graph[idx][c] == 0:
                        graph[idx][c] = temp
                    else:
                        idx -= 1
                        graph[idx][c] = temp
    elif d == 2:  # left
        for r in range(n):
            idx = 0
            for c in range(1, n):
                if graph[r][c]:
                    temp = graph[r][c]
                    graph[r][c] = 0
                    if graph[r][idx] == temp:
                        graph[r][idx] = 2 * temp
                        idx += 1
                    elif graph[r][idx] == 0:
                        graph[r][idx] = temp
                    else:
                        idx += 1
                        graph[r][idx] = temp
    elif d == 3:  # right
        for r in range(n):
            idx = n - 1
            for c in range(n - 2, -1, -1):
                if graph[r][c]:
                    temp = graph[r][c]
                    graph[r][c] = 0
                    if graph[r][idx] == temp:
                        graph[r][idx] = 2 * temp
                        idx -= 1
                    elif graph[r][idx] == 0:
                        graph[r][idx] = temp
                    else:
                        idx -= 1
                        graph[r][idx] = temp


def dfs(cnt):
    global answer, graph
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, graph[i][j])
        return

    tempG = deepcopy(graph)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        graph = deepcopy(tempG)


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
dfs(0)
print(answer)