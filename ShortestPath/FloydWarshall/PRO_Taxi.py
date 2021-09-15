def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(len(fares)):
        graph[fares[i][0]][fares[i][1]] = graph[fares[i][1]][fares[i][0]] = fares[i][2]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

    answer = INF
    for i in range(1, n + 1):
        via = graph[s][i] + graph[i][b] + graph[i][a]
        answer = min(answer, via)

    return answer