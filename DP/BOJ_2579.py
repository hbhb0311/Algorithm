n = int(input())
stair = []
d = []

for _ in range(n):
    stair.append(int(input()))

if n == 1:
    d.append(stair[0])

elif n == 2:
    d.append(stair[0])
    d.append(stair[0] + stair[1])

elif n == 3:
    d.append(stair[0])
    d.append(stair[0] + stair[1])
    d.append(max(stair[0], stair[1]) + stair[2])

else:
    d.append(stair[0])
    d.append(stair[0] + stair[1])
    d.append(max(stair[0], stair[1]) + stair[2])

    for i in range(3, n):
        d.append(max(d[i - 2] + stair[i], d[i - 3] + stair[i - 1] + stair[i]))

print(d[-1])