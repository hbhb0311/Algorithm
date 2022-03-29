def dfs(numbers, target, result, cnt):
    global answer 
    
    if cnt == len(numbers) and result == target:
        answer += 1
        return
    
    if cnt == len(numbers):
        return
    
    dfs(numbers, target, result + numbers[cnt], cnt+1)
    dfs(numbers, target, result - numbers[cnt], cnt+1)


def solution(numbers, target):
    global answer 
    answer = 0
    
    dfs(numbers, target, 0, 0)
    return answer 
        

print(solution([4, 1, 2, 1], 4))
print(solution([1, 1, 1, 1, 1], 3))