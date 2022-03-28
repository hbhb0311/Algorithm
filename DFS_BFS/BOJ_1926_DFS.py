import sys
sys.setrecursionlimit(10000000)

def dfs(x, y):
    global cnt
    cnt += 1
    paint[x][y] = 0

    for i in d:
        nx = x + i[0]
        ny = y + i[1]

        if 0 <= nx < n and 0 <= ny < m and paint[nx][ny] == 1:
            dfs(nx, ny)


input = sys.stdin.readline
n, m = map(int, input().split())
paint = []
cntlst = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    paint.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1:
            cnt = 0
            dfs(i, j)
            cntlst.append(cnt)

if len(cntlst) == 0:
    print(0)
    print(0)
else:
    print(len(cntlst))
    print(max(cntlst))





######### 시간 초과 발생
def dfs(x, y):
    global cnt
    visited.append((x, y))
    for i in d:
        nx = x + i[0]
        ny = y + i[1]

        if 0 <= nx < n and 0 <= ny < m and paint[nx][ny] == 1 and (nx, ny) not in visited:
            visited.append((nx, ny))
            cnt += 1
            dfs(nx, ny)


input = sys.stdin.readline
n, m = map(int, input().split())
paint = []
visited = []
cntlst = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    paint.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1 and (i, j) not in visited:
            cnt = 1
            dfs(i, j)
            cntlst.append(cnt)

if len(cntlst) == 0:
    print(0)
    print(0)
else:
    print(len(cntlst))
    print(max(cntlst))
