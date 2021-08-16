def solution(lottos, win_nums):
    rank = {0: 6}

    for i in range(1, 7):
        rank[i] = 7 - i

    min_count = len(list(set(lottos).intersection(win_nums)))
    max_count = min_count + lottos.count(0)

    answer = [rank[max_count], rank[min_count]]
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
