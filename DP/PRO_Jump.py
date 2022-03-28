def solution(n):
    cnt = 0

    while n > 0:
        q = n // 2

        if n % 2 != 0:
            cnt += 1
        n = q

    return cnt



######### 시간 초과 발생
def solution(n):
    dp = []

    for i in range(n + 1):
        dp.append(i)

    for i in range(2, len(dp)):
        dp[i] = min(dp[i], dp[i - 1] + 1)

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2])

    return dp[n]




###### 다른 사람의 풀이
def solution(n):
    return bin(n).count('1')

print(solution(5000))