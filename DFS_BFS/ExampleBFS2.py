from collections import deque
def bfs(start):
    visited.append(start)
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)


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

visited = []
bfs(1)

for i in range(len(visited)):
    print(visited[i], end = ' ')