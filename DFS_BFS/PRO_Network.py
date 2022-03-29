from collections import defaultdict
def dfs(num, graph, visited):
    visited[num] = True
    if num not in graph.keys(): return

    for i in graph[num]:
        if not visited[i]:
            dfs(i, graph, visited)

def solution(n, computers):
    graph = defaultdict(list)    
    visited = [False] * n
    answer = 0
    for idx in range(n):
        for i, v in enumerate(computers[idx]):
            if idx == i: continue
            if v == 1: graph[idx].append(i)

    while False in visited:
        dfs(visited.index(False), graph, visited)
        answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))