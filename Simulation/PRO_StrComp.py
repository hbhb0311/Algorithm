def solution(s):
    if len(s) == 1:
        return 1

    else:
        result = []
        temp = ""
        cnt = 1

        for i in range(1, len(s) // 2 + 1):
            for j in range(0, len(s), i):
                if s[j: j + i] == s[j + i: j + 2 * i]:
                    cnt += 1
                else:
                    if cnt > 1:
                        temp += str(cnt) + s[j: j + i]
                        cnt = 1
                    else:
                        temp += s[j: j + i]
                        cnt = 1
            result.append(len(temp))
            temp = ""
        return min(result)

print(solution("abcabcabcabcdededededede"))


