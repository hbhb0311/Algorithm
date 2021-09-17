import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
ans = int(1e9)

for _ in range(n):
    string = input().rstrip()
    graph.append(string)

for k in range(n - 7):
    for j in range(m - 7):
        wcnt, bcnt = 0, 0
        for i in range(8):
            cnt = 0
            for g in graph[k + i][j: j + 8]:
                if (k + i) % 2 == 0:
                    if cnt % 2 == 0:
                        if g == 'W':
                            bcnt += 1
                        else:
                            wcnt += 1
                    else:
                        if g == 'W':
                            wcnt += 1
                        else:
                            bcnt += 1

                else:
                    if cnt % 2 == 0:
                        if g == 'W':
                            wcnt += 1
                        else:
                            bcnt += 1
                    else:
                        if g == 'W':
                            bcnt += 1
                        else:
                            wcnt += 1
                cnt += 1
        ans = min(wcnt, bcnt, ans)
print(ans)