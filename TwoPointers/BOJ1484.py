import sys
input = sys.stdin.readline

G = int(input())
numbers = [x ** 2 for x in range(1, 100001)]

start, end = 0, 1
ans = []

while True:
    if end - start == 1 and numbers[end] - numbers[start] > 100000:
        break

    if numbers[end] - numbers[start] > G:
        start += 1

    elif numbers[end] - numbers[start] < G:
        end += 1

    else:
        ans.append(end + 1)
        start += 1

if ans:
    for i in ans: print(i)
else:
    print(-1)