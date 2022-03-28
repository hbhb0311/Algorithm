import sys
input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

summ = 0
start = 0
end = 0
lenn = N + 1

for start in range(N):
    while summ < S and end < N:
        summ += seq[end]
        end += 1

    if summ >= S:
        lenn = min(lenn, len(seq[start : end]))

    summ -= seq[start]


if lenn == N + 1:
    print(0)
else:
    print(lenn)

