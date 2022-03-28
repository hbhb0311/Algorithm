n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in trees:
        if (i - mid) > 0:
            total += (i - mid)

    if total < m:
        end = mid - 1

    else:
        start = mid + 1
        result = mid

print(result)