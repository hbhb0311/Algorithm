import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    result = sum(list(map(int, str(i))))
    result += i

    if result == n:
        print(i)
        break
    elif i == n:
        print(0)