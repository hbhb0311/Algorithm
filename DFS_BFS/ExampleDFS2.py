def dfs(idx):

    for i in graph[idx]:
        if i not in visited:
            visited.append(i)
            dfs(i)

graph = [
         [],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
]


visited = [1]
dfs(1)
for i in range(len(visited)):
    print(visited[i], end = ' ')