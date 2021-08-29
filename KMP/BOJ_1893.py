import sys
input = sys.stdin.readline


def getPi(keyword):
    keywordLength = len(keyword)
    pi = [0] * keywordLength
    j = 0

    for i in range(1, keywordLength):
        while j > 0 and keyword[i] != keyword[j]:
            j = pi[j-1]

        if keyword[i] == keyword[j]:
            j += 1
            pi[i] = j
    return pi


def shift_order():
    aLength = len(A)
    shiftedChar = {}

    for i in range(aLength):
        shiftedChar[A[i]] = A[i-1]

    return shiftedChar


def printcntlst():
    cntlst = []
    aLength = len(A)
    Schanged = S

    if cntcheck(Schanged, W):
        cntlst.append(0)

    for i in range(1, aLength):
        Schanged = shift(Schanged)

        if cntcheck(Schanged, W):
            cntlst.append(i)

    cntlstLength = len(cntlst)

    if cntlstLength == 0:
        print("no solution")
    elif cntlstLength == 1:
        print("unique:", cntlst[0])
    else:
        print("ambiguous:", end="")
        for n in cntlst:
            print("", n, end="")
        print()

def cntcheck(string, keyword):
    cnt = 0
    strLength = len(string)
    keyLength = len(keyword)

    i = 0
    for j in range(strLength):
        while i > 0 and keyword[i] != string[j]:
            i = pi[i - 1]

        if keyword[i] == string[j]:
            if i == keyLength - 1:
                cnt += 1
                i = pi[i]
                if cnt > 1:
                    return False
            else:
                i += 1
    return cnt == 1

def shift(s):
    shifted = s
    length = len(s)

    for i in range(length):
        shifted[i] = leftShiftedChar[shifted[i]]

    return shifted


N = int(input())
for _ in range(N):
    A, W, S = list(input().rstrip()), list(
        input().rstrip()), list(input().rstrip())

    pi = getPi(W)
    leftShiftedChar = shift_order()
    printcntlst()