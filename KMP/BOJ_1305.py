import sys
input = sys.stdin.readline

L = int(input())
S = input().rstrip()

i = 0
pi = [0] * L
for j in range(1, L):
    while i > 0 and S[i] != S[j]:
        i = pi[i - 1]

    if S[i] == S[j]:
        i += 1
        pi[j] = i

print(L - pi[-1])