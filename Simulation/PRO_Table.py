from collections import deque

def solution(n, k, cmd):
    deleted = deque()
    linked_lst = []

    for i in range(n):
        linked_lst.append([i - 1, i + 1])

    for c in cmd:
        route = c.split(' ')

        if route[0] == 'U':
            for _ in range(int(route[1])):
                k = linked_lst[k][0]

        elif route[0] == 'D':
            for _ in range(int(route[1])):
                k = linked_lst[k][1]

        elif route[0] == 'C':
            deleted.append((k, linked_lst[k]))

            if linked_lst[k][0] != -1:
                linked_lst[linked_lst[k][0]][1] = linked_lst[k][1]

            if linked_lst[k][1] != n:
                linked_lst[linked_lst[k][1]][0] = linked_lst[k][0]

            if linked_lst[k][1] == n:
                k = linked_lst[k][0]
            else:
                k = linked_lst[k][1]

        elif route[0] == 'Z':
            last = deleted.pop()

            if last[1][1] != n:
                linked_lst[last[1][1]][0] = last[0]

            if last[1][0] != -1:
                linked_lst[last[1][0]][1] = last[0]

    answer = ['O'] * n

    for d in deleted:
        answer[d[0]] = 'X'

    return ''.join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
