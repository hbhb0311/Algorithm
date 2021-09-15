i = 0

while True:
    cnt = 0
    l, p, v = map(int, input().split())

    if l == p == v == 0:
        break

    cnt += v // p
    cnt *= l
    i += 1

    if (v % p < l):
        cnt += v % p
    else:
        cnt += l

    print(f'Case {i}: {cnt}')