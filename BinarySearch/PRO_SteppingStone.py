def solution(stones, k):
    start = 1
    end = max(stones)
    answer = int(1e9)

    while start <= end:
        flag = False
        mid = (start + end) // 2
        cnt = 0

        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt == k:
                    flag = True
                    break
            else:
                cnt = 0

        if flag:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer