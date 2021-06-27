import sys
input = sys.stdin.readline

x = input()
row = ord(x[0]) - ord('a') + 1
col = int(x[1])
route = [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0

for val in route:
    if row + val[0] >= 1 and row + val[0] <= 8 and col + val[1] >= 1 and col + val[1] <= 8:
        cnt += 1

print(cnt)