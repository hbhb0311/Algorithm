import sys
input = sys.stdin.readline

N, d, k, coupon = map(int, input().split())
cnt = 0
dish = []

for _ in range(N):
    dish.append(int(input()))

for i in range(k - 1):
    dish.append(dish[i])

start = 0
end = k

for i in range(N):
    temp = dish[start : end]
    temp.append(coupon)

    cnt = max(cnt, len(set(temp)))
    start += 1
    end += 1

print(cnt)





##### 슬라이딩 윈도우 ??
import sys
from collections import deque

input = sys.stdin.readline

N, d, k, coupon = map(int, input().split())
cnt = 0
dish = []

for _ in range(N):
    dish.append(int(input()))

for i in range(k - 1):
    dish.append(dish[i])


window = deque(dish[0 : k])
for i in range(N - 1):
    window.append(coupon)
    cnt = max(cnt, len(set(window)))
    window.pop()
    window.popleft()
    window.append(dish[i + k])

print(cnt)
