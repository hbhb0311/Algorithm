import heapq
def solution(food_times, k):
    answer = -1
    ft = []

    for i in range(len(food_times)):
        heapq.heappush(ft, (food_times[i], i + 1))

    pre = 0
    num_re = len(food_times)

    while ft:
        time = (ft[0][0] - pre) * num_re

        if k >= time:
            k -= time
            pre, _ = heapq.heappop(ft)
            num_re -= 1

        else:
            ft.sort(key = lambda x : x[1])
            answer = ft[k % num_re][1]
            break

    return answer

print(solution([2, 7, 5, 3], 14))