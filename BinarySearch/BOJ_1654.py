k, n = map(int, input().split())
lst = []

for _ in range(k):
    lst.append(int(input()))

start = 1
end = max(lst)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(k):
        cnt += lst[i] // mid

    if cnt < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)