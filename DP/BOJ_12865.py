n, k = map(int, input().split())
stuff = [[0, 0]]
d = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(value + d[i - 1][j - weight], d[i - 1][j])

print(d[n][-1])