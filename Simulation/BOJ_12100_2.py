import sys
from copy import deepcopy
input = sys.stdin.readline

def move():
    global graph
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

def rotate(cnt):
    global graph
    for _ in range(cnt):
        temp_g = deepcopy(graph)
        for r in range(n):
            for c in range(n):
                temp_g[c][n - 1 - r] = graph[r][c]
        graph = deepcopy(temp_g)

def dfs(cnt):
    global answer, graph
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, graph[i][j])
        return

    tempG = deepcopy(graph)
    for i in range(4):
        rotate(i)
        move()
        dfs(cnt + 1)
        graph = deepcopy(tempG)


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
dfs(0)
print(answer)
