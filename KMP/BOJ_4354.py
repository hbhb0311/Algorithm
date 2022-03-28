import sys
input = sys.stdin.readline

def pi(pat):
    pat = list(pat)
    pilst = [0] * len(pat)
    i = 0

    for j in range(1, len(pat)):
        while i > 0 and pat[i] != pat[j]:
            i = pilst[i - 1]

        if pat[i] == pat[j]:
            i += 1
            pilst[j] = i

    return pilst

while True:
    s = input().rstrip()

    if s == '.':
        break

    pilst = pi(s)
    if len(s) % (len(s) - pilst[-1]) == 0:
        print(len(s) // (len(s) - pilst[-1]))
    else:
        print(1)