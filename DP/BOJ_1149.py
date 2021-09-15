########### 혼자 풀어오기 -> 인덱스를 기준으로 가져오니 에러발생
import copy

n = int(input())
house = []

for i in range(n):
    house.append(list(map(int, input().split())))

cost = []
for i in range(len(house[0])):
    house_c = copy.deepcopy(house)
    cost.append(house_c[0][i])
    idx = i
    for j in range(1, len(house)):
        house_c[j][idx] = 1001
        idx = house_c[j].index(min(house_c[j]))
        cost[i] += min(house_c[j])

print(min(cost))



########### 블로그 참고한 코드

n = int(input())
house = []

for i in range(n):
    house.append(list(map(int, input().split())))

for i in range(1, len(house)):
    house[i][0] = min(house[i - 1][1], house[i - 1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]
    house[i][2] = min(house[i - 1][0], house[i - 1][1]) + house[i][2]

print(min(house[n - 1][0], house[n - 1][1], house[n - 1][2]))