def solution(N, number):
    set_full = [0, [N]]

    if number == N:
        return 1

    for i in range(2, 9):
        set_i = []
        set_i.append(int(str(N) * i))

        for j in range(1, i // 2 + 1):
            for x in set_full[j]:
                for y in set_full[i - j]:
                    set_i.append(x + y)
                    set_i.append(x - y)
                    set_i.append(y - x)
                    set_i.append(x * y)

                    if x != 0:
                        set_i.append(y // x)
                    if y != 0:
                        set_i.append(x // y)

        if number in set_i:
            return i

        set_full.append(set_i)

    return -1