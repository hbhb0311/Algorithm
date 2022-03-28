##### 시간 초과 ####

import sys
from collections import deque

input = sys.stdin.readline
lst = list(input().rstrip())
q = deque()
dot = []
line = []

for idx, val in enumerate(lst):
    if val == ')':
        left = q.pop()
        if left == idx - 1:
            dot.append([idx-1, idx])
        else:
            line.append([left, idx])
    else:
        q.append(idx)

ans = 0
for l in line:
    cnt = 0
    for d in dot:
        if d[1] < l[0] or d[0] > l[1]:
            continue
        cnt += 1
    ans += cnt + 1
print(ans)



#### count 방법 변경 ####

import sys
from collections import deque

input = sys.stdin.readline
lst = list(input().rstrip())
q = deque()

ans = 0
for i in range(len(lst)):
    if lst[i] == '(':
        q.append(lst[i])
    else:
        if lst[i-1] == '(':
            q.pop()
            ans += len(q)
        else:
            q.pop()
            ans += 1

print(ans)