########### 최종 제출 - 슬라이딩 윈도우

import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
Alst = list(map(int, input().split()))
window = deque()

for i in range(N):
    while window and window[-1][1] > Alst[i]:
        window.pop()
    window.append((i, Alst[i]))

    if i >= L and window[0][0] == i - L:
        window.popleft()

    print(window[0][1], end = ' ')



########### 시간 초과 발생

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
Alst = list(map(int, input().split()))

window_min = int(1e9)
window_start = 0

for window_end in range(N):
    window_min = min(window_min, Alst[window_end])

    if window_end >= L:
        window_start += 1
        window_min = min(Alst[window_start : window_end + 1])

    print(window_min, end = ' ')



########### 시간 초과 발생
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
Alst = list(map(int, input().split()))
Alst.insert(0, 0)
ans = []

for i in range(1, N + 1):
    if i - L + 1 < 1:
        start = 1
    else:
        start = i - L + 1
    end = i
    ans.append(min(Alst[start : end + 1]))

for i in ans: print(i, end = ' ')