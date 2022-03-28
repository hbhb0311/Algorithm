n, l = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

cnt = 1
length = 0

for i in range(len(loc) - 1):
    if (length + loc[i + 1] - loc[i] + 1) <= l:
        length += loc[i + 1] - loc[i]

    else:
        cnt += 1
        length = 0

print(cnt)