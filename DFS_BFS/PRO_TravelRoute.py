from collections import defaultdict
def solution(tickets):
    tickets.sort(key = lambda x: x[1])
    route = defaultdict(list)
    answer, stack = [], []
    
    for start, end in tickets:
        route[start].append(end)
    
    stack.append('ICN')
    while stack:
        if not route[stack[-1]]:
            answer.append(stack.pop())
        else:
            stack.append(route[stack[-1]].pop(0))
    return answer[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL","SFO"], ["ATL", "ICN"]]))