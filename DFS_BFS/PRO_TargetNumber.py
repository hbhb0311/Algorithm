from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    cnt = 0
    
    while queue:
        number, count = queue.popleft()
        count += 1
        if count < len(numbers):
            queue.append([number + numbers[count], count])
            queue.append([number - numbers[count], count])
        else:
            if number == target:
                cnt += 1
    return cnt

print(solution([4, 1, 2, 1], 4))
print(solution([1, 1, 1, 1, 1], 3))