def solution(cookie):
    answer = 0
    N = len(cookie)

    for i in range(N - 1):
        idx_l, sum_l = i, cookie[i]
        idx_r, sum_r = i + 1, cookie[i + 1]

        while True:
            if sum_l == sum_r:
                answer = max(answer, sum_l)

            if idx_l > 0 and sum_l <= sum_r:
                idx_l -= 1
                sum_l += cookie[idx_l]

            elif idx_r < N - 1 and sum_l >= sum_r:
                idx_r += 1
                sum_r += cookie[idx_r]

            else:
                break
    return answer





############### 다른 사람의 풀이
from itertools import accumulate
def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c:
            answer = max(*c, answer)
    return answer

print(solution([500, 250, 250, 500, 500, 100]))