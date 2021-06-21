# 효율성 테스트 실패

from collections import deque

def solution(stones, k):
    window = deque(stones[ :k])
    window_max = max(window)
    minn = window_max

    for i in range(k, len(stones)):
        leftpop = window.popleft()
        window.append(stones[i])

        if leftpop == window_max:
            window_max = max(window)
            minn = min(minn, window_max)
    return minn

# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))