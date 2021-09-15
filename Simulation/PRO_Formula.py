############ 블로그 참고
from itertools import permutations
def calc(op, seq, exp):
    if exp.isdigit():
        return str(exp)

    else:
        if op[seq] == '*':
            splt = exp.split('*')
            temp = []
            for s in splt:
                temp.append(calc(op, seq + 1, s))

            return str(eval('*'.join(temp)))

        if op[seq] == '+':
            splt = exp.split('+')
            temp = []
            for s in splt:
                temp.append(calc(op, seq + 1, s))

            return str(eval('+'.join(temp)))

        if op[seq] == '-':
            splt = exp.split('-')
            temp = []
            for s in splt:
                temp.append(calc(op, seq + 1, s))

            return str(eval('-'.join(temp)))


def solution(exp):
    op_pri = list(permutations(['*', '-', '+'], 3))
    answer = 0

    for op in op_pri:
        answer = max(answer, abs(int(calc(op, 0, exp))))

    return answer