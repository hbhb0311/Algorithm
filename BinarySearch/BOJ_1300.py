N = int(input())
k = int(input())
start, end = 1, k
ans = 0

while start <= end:
    mid = (start + end) // 2

    res = 0
    for i in range(1, N + 1):
        res += min(mid // i, N)

    if res >= k:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)