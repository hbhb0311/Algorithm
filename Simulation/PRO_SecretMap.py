###### if else
def solution(n, arr1, arr2):
    answer = []
    bit1 = []
    bit2 = []

    for i in range(n):
        bit1.append(format(arr1[i], 'b').zfill(n))
        bit2.append(format(arr2[i], 'b').zfill(n))

    for i in range(n):
        result = ""
        for j in range(n):
            if int(bit1[i][j]) == 0 and int(bit2[i][j]) == 0:
                result += ' '
            else:
                result += '#'

        answer.append(result)

    return answer



######### binary
def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        result = str(bin(i | j)[2: ]).zfill(n)
        result = result.replace('1', '#')
        result = result.replace('0', ' ')
        answer.append(result)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))