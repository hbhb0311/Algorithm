# 효율성 실패 ㅠㅠ..
# 리스트 자체에서 값을 제외하면 효율성 실패 발생한다고 함

def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    for i, val in enumerate(people):
        for j in range(i + 1, len(people)):
            if people[i] + people[j] <= limit:
                del people[j]
                break

        answer += 1

    return answer



########## 블로그 참고한 코드

def solution(people, limit):
    people.sort()
    answer = 0
    i, j = 0, len(people) - 1

    while True:
        if i > j:
            break
        answer += 1

        if (people[i] + people[j]) <= limit:
            i += 1
        j -= 1

    return answer