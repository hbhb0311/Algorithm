import sys
input = sys.stdin.readline

N = int(input())
route = list(input().split())
move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1

for r in route:
    for i in range(len(move)):
        if r == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x, y = nx, ny

print(x, y)