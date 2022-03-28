from string import ascii_uppercase

def solution(msg):
    answer = []
    msg += '!'
    alpha = list(ascii_uppercase)
    alpha.insert(0, 0)
    result = 0
    print(alpha)

    while msg != '!':
        idx = 1
        while msg[:idx] in alpha:
            result = alpha.index(msg[:idx])
            idx += 1

        answer.append(result)
        alpha.append(msg[:idx])
        msg = msg[idx - 1:]

    return answer

print(solution('KAKAO'))