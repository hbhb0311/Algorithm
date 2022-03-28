import sys
input = sys.stdin.readline

def pi(p):
    i = 0
    pilst = [0] * len(p)
    for j in range(1, len(p)):
        while i > 0 and p[i] != p[j]:
            i = pilst[i - 1]

        if p[i] == p[j]:
            i += 1
            pilst[j] = i
    return pilst

text, pattern = list(input().rstrip()), list(input().rstrip())
i = 0
idxlst = []
pilst = pi(pattern)

for j in range(len(text)):
    while i > 0 and text[j] != pattern[i]:
        i = pilst[i - 1]

    if text[j] == pattern[i]:
        if i == len(pattern) - 1:
            idxlst.append(j - len(pattern) + 2)
            i = pilst[i]
        else:
            i += 1
print(len(idxlst))
for i in idxlst:
    print(i, end = " ")