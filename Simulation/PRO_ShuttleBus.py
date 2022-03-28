def solution(n, t, m, timetable):
    timemin = []
    bus = []

    for time in timetable:
        timemin.append(int(time[ : 2]) * 60 + int(time[3: 5]))
    timemin.sort()

    for i in range(9 * 60, 9 * 60 + n * t, t):
        bus.append(i)

    cnt, lastT = 0, 0
    for b in bus:
        cnt = 0
        for t in timemin:
            if t <= b:
                cnt += 1

            if cnt == m:
                lastT = t
                break

        timemin = timemin[cnt : ]

    if cnt >= m:
        result = lastT - 1
    else:
        result = bus[-1]

    answer = str(result // 60).zfill(2) + ":" + str(result % 60).zfill(2)
    return answer

print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))