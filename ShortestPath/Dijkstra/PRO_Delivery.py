import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    answer = 0

    for r in road:
        graph[r[0]].append((r[2], r[1]))
        graph[r[1]].append((r[2], r[0]))

    INF = int(1e9)
    distance = [INF] * (N + 1)

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for g in graph[now]:
            cost = dist + g[0]

            if cost < distance[g[1]]:
                distance[g[1]] = cost
                heapq.heappush(q, (cost, g[1]))

    for d in distance:
        if d <= K:
            answer += 1

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))