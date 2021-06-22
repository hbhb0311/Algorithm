####### 슬라이딩 윈도우로 풀이!

from collections import deque

def solution(stones, k):
    window = deque()
    result = []

    for i in range(len(stones)):
        while window and window[-1][1] < stones[i]:
            window.pop()
        window.append((i, stones[i]))

        if i >= k and window[0][0] == i - k:
            window.popleft()

        if i >= k - 1:
            result.append(window[0][1])

    return min(result)

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))





############# 효율성 테스트 실패

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