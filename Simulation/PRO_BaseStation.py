import math

def solution(n, stations, w):
    answer = 0
    dist = []

    for i in range(1, len(stations)):
        dist.append(stations[i] - 1 - stations[i - 1] - 2 * w)  # stations[i] - w - 1 - (stations[i - 1] + w)

    dist.append(stations[0] - w - 1)
    dist.append(n - (stations[-1] + w))

    for d in dist:
        if d < 1:
            continue

        answer += math.ceil(d / (2 * w + 1))

    return answer

print(solution(11, [4, 11], 1))