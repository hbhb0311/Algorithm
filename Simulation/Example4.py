import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B, d = map(int, input().split())
D = [[0] * M for _ in range(N)]
D[A][B] = 1

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
cnt = 1

while True:
    for _ in range(4):
        d += 1
        if d == 4:
            d = 0

        nA = A + dir[d][0]
        nB = B + dir[d][1]
        try:
            if D[nA][nB] == 0 and graph[nA][nB] == 0 and nA >= 0 and nA < N and nB >= 0 and nB < M:
                A, B = nA, nB
                D[nA][nB] = 1
                cnt += 1
                break
        except IndexError:
            continue
    else:
        nA = A - dir[d][0]
        nB = B - dir[d][1]

        try:
            if D[nA][nB] == 0 and nA >= 0 and nA < N and nB >= 0 and nB < M:
                A, B = nA, nB
        except IndexError:
            continue

        else:
            break

print(cnt)
