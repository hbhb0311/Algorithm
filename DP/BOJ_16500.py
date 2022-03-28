########## 블로그 참고
def dpfunc(idx):
    global res
    if idx == len(S):
        res = 1
        return

    if dp[idx]:
        return

    dp[idx] = 1
    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]):
            for j in range(len(A[i])):
                if A[i][j] != S[idx + j]:
                    break
            else:
                dpfunc(idx + len(A[i]))

    return


S = input()
N = int(input())
A = []

for _ in range(N):
    A.append(input())

dp = [0] * 101
res = 0
dpfunc(0)
print(res)