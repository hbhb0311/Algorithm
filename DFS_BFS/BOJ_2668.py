import sys
def dfs(start):
    visited.append(start)
    if arr[start] not in visited:
        dfs(arr[start])
    else:
        if arr[start] == samenum:
            intlst.append(samenum)


input = sys.stdin.readline

n = int(input())
arr = [0]
intlst = []

for _ in range(n):
    arr.append(int(input()))

for i in range(1, n + 1):
    visited = []
    samenum = i
    dfs(i)

print(len(intlst))
for i in intlst:
    print(i)

