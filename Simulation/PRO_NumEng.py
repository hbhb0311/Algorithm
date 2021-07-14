def solution(s):
    number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = ""
    idx = 0

    for i in range(len(s)):
        try:
            if type(int(s[i])) == int:
                answer += str(s[i])
                idx = i + 1
        except:
            if s[idx : i + 1] in number.keys():
                answer += str(number[s[idx : i + 1]])
                idx = i + 1
    return int(answer)

print(solution("one4seveneight"))



######## 다른 사람의 풀이
number = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def solution(s):
    answer = s

    for key, value in number.items():
        answer = answer.replace(key, value)

    return int(answer)

print(solution("one4seveneight"))