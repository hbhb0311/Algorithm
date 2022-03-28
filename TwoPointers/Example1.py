"""
특정한 합을 가지는 부분 연속 수열 찾기 문제
부분합이 m보다 작으면 end += 1, m보다 크면 start += 1
"""

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)