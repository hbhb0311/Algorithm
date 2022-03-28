# 책에 나와있는 풀이
import sys
input = sys.stdin.readline

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)




# 내가 푼 풀이
import sys
input = sys.stdin.readline

N = int(input())
hour, min, sec = 0, 0, 0
cnt = 0

while True:
    sec += 1

    if sec == 60:
        sec = 0
        min += 1

    if min == 60:
        min = 0
        hour += 1

    if hour == N + 1:
        break

    if ('3' in str(hour)) or ('3' in str(min)) or ('3' in str(sec)):
        cnt += 1

print(cnt)
