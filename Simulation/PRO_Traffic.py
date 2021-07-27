def solution(lines):
    time = []
    for i in lines:
        end = (int(i[11 : 13]) * 3600 + int(i[14 : 16]) * 60 + int(i[17 : 19])) * 1000 + int(i[20 : 23])
        start = int(end - float(i[24: -1]) * 1000 + 1)
        time.append([start, end])

    answer = 0
    for t in time:
        cnt = 0
        s = t[0]
        e = t[0] + 1000

        for tt in time:
            if tt[0] < e and tt[1] >= s:
                cnt += 1
        answer = max(answer, cnt)

    for t in time:
        cnt = 0
        s = t[1]
        e = t[1] + 1000

        for tt in time:
            if tt[0] < e and tt[1] >= s:
                cnt += 1
        answer = max(answer, cnt)

    return answer


print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))