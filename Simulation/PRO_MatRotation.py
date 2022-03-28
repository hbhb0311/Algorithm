from copy import deepcopy

def solution(rows, columns, queries):
    graph = [[-1] * columns]
    answer = []

    for i in range(1, rows * columns + 1, columns):
        lst = [-1]
        for j in range(columns):
            lst.append(i + j)
        graph.append(lst)

    graph_c = deepcopy(graph)

    for q in queries:
        x1, y1, x2, y2 = q
        dy = y2 - y1
        dx = x2 - x1

        graph_c[x1][y1 + 1 : y1 + dy + 1] = graph[x1][y1 : y1 + dy]
        result = min(graph[x1][y1 : y1 + dy])

        graph_c[x2][y1 : y1 + dy] = graph[x2][y1 + 1 : y1 + dy + 1]
        minval = min(graph[x2][y1 + 1 : y1 + dy + 1])
        result = min(result, minval)

        for i in range(dx):
            graph_c[x1 + i][y1] = graph[x1 + i + 1][y1]
            graph_c[x1 + i + 1][y2] = graph[x1 + i][y2]
            result = min(result, graph[x1 + i + 1][y1], graph[x1 + i][y2])

        graph = deepcopy(graph_c)
        answer.append(result)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))

