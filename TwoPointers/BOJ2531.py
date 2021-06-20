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
