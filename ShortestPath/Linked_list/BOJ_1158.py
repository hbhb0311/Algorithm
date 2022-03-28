import sys
input = sys.stdin.readline

n, ori_k = map(int, input().split())

def Josephus(n, ori_k):
    linked_lst = [[]]
    deleted = []

    if n == 1:
        print('<1>')
        return

    for i in range(1, n + 1):
        if i == 1:
            linked_lst.append([n, i + 1])
        elif i == n:
            linked_lst.append([i - 1, 1])
        else:
            linked_lst.append([i - 1, i + 1])

    k = ori_k
    for _ in range(n):
        deleted.append(k)
        linked_lst[linked_lst[k][0]][1] = linked_lst[k][1]
        linked_lst[linked_lst[k][1]][0] = linked_lst[k][0]

        for _ in range(ori_k):
            k = linked_lst[k][1]

    print('<', end = '')
    for i in range(n):
        if i == n - 1:
            print(deleted[i], end = '')
        else:
            print(deleted[i], end = ', ')
    print('>')

Josephus(n, ori_k)




