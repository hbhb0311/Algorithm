# 균형잡힌 괄호 무자열 u, v로 분리하는 함수
def uv(p):
    lcnt, rcnt = 0, 0

    for i in range(len(p)):
        if p[i] == '(':
            lcnt += 1
        else:
            rcnt += 1

        if lcnt == rcnt:
            return p[:i + 1], p[i + 1:]

# u가 "올바른 괄호 문자열"인지 판별하는 함수
def isbalanced(temp):
    while True:
        lenn = len(temp)

        if lenn == 0:
            return True
        for i in range(lenn - 1):
            if temp[i] == '(' and temp[i + 1] == ')':
                del temp[i]
                del temp[i]
                break
        else:
            return False


def solution(p):

    # 1단계 : 빈 문자열인 경우, 빈 문자열 반환
    if not p:
        return ""

    # 2단계 : 균형잡힌 괄호 문자열 u, v로 분리
    u, v = uv(p)
    temp = list(u)

    # 3단계 : u가 올바른 괄호 문자열이면 문자열 v에 대해 1단계부터 다시 수행
    if isbalanced(temp):
        # 3-1단계 - 수행한 결과 문자열을 u에 이어 붙인 후 반환
        return u + solution(v)

    # 4단계 : 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정 수행
    else:

        # 4-1단계 : 빈 문자열에 첫 번째 문자로 '('를 붙임
        answer = "("
        # 4-2단계 : 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
        answer += solution(v)
        # 4-3단계 : ')'를 다시 붙임
        answer += ")"

        # 4-4단계 : u의 첫 번째와 마지막 문자 제거 후, 나머지 문자열의 괄호 방향 뒤집어 뒤에 붙임
        utemp = ""
        for i in u[1 : -1]:
            if i == "(":
                utemp += ")"
            else:
                utemp += "("

        answer += utemp

        # 4-5단계 : 생성된 문자열을 반환
        return answer

print(solution("()))((()"))