import sys
input = sys.stdin.readline

n, k = map(int, input().split())
plug = list(map(int, input().split()))
cnt = 0

cur = []
for i in range(k):
    if plug[i] not in cur:
        cur.append(plug[i])
    if len(cur) == n:
        break
plug.extend(set(plug))

for i in range(n, k):
    if plug[i] in cur:
        continue
    else:
        ans = cur[0]
        for c in cur[1:]:
                if plug.index(c, i) > plug.index(ans, i):
                    if plug.index(ans, i) > k: break
                    else: ans = c
        cur.remove(ans)
        cur.append(plug[i])
        cnt += 1
print(cnt)