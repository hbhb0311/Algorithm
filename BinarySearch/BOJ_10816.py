# 시간초과 발생..

def binary(start, end, array, target):
    cnt = 0

    if start > end:
        return 0

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            cnt += 1
            array[mid] = int(1e9)
            array.sort()

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return cnt

n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
sang = list(map(int, input().split()))

for i in range(m):
    print(binary(0, m - 1, card, sang[i]), end = ' ')