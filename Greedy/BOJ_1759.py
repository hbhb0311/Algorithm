import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
char = list(input().split())
char.sort()

sortedChar = list(map(''.join, combinations(char, l)))
for c in sortedChar:
    cnt = 0
    for i in c:
        if i in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    if l - cnt >= 2 and cnt >= 1:
        print(c)