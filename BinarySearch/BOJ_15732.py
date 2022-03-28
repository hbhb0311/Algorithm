############# 메모리 초과

N, K, D = map(int, input().split())
d = []

for _ in range(K):
    A, B, C = map(int, input().split())

    for i in range(A, B + 1, C):
        d.append(i)

d.sort()
print(d[D - 1])




####### 고친 풀이
N, K, D = map(int, input().split())
lst = []

for _ in range(K):
    lst.append(list(map(int, input().split())))

start, end = 1, N
ans = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(K):
        midd = min(lst[i][1], mid)
        if (midd - lst[i][0]) >= 0:
            cnt += (midd - lst[i][0]) // lst[i][2] + 1

    if cnt < D:
        start = mid + 1

    else:
        ans = mid
        end = mid - 1
print(ans)