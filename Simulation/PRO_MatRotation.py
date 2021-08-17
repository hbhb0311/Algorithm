def solution(rows, columns, queries):
    graph = [[-1] * columns]
    answer = []

    for i in range(1, rows * columns + 1, columns):
        lst = [-1]
        for j in range(columns):
            lst.append(i + j)
        graph.append(lst)

    for x1, y1, x2, y2 in queries:
        popval = graph[x1][y1]
        result = popval

        for i in range(x1, x2):
            graph[i][y1] = graph[i + 1][y1]
            temp = graph[i + 1][y1]
            result = min(result, temp)

        for i in range(y1, y2):
            graph[x2][i] = graph[x2][i + 1]
            temp = graph[x2][i + 1]
            result = min(result, temp)

        for i in range(x2, x1, -1):
            graph[i][y2] = graph[i - 1][y2]
            temp = graph[i - 1][y2]
            result = min(result, temp)

        for i in range(y2, y1, -1):
            graph[x1][i] = graph[x1][i - 1]
            temp = graph[x1][i - 1]
            result = min(result, temp)

        graph[x1][y1 + 1] = popval
        answer.append(result)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))