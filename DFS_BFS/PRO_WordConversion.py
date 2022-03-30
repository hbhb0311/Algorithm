from collections import deque, defaultdict
def diff(str1, str2):
    diffNum = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            diffNum += 1
       
        if diffNum > 1: 
            return False
    return True

def bfs(begin, target, words, graph):
    visited = dict.fromkeys(words, False)
    queue = deque([[begin, 0]])
    visited[begin] = True
    answer = 0
    
    while queue:
        before, result = queue.popleft()
        if before == target:
            answer = result
            return answer
        
        for word in graph[before]:
            if not visited[word]:
                queue.append([word, result + 1])
                visited[word] = True
    return answer
    
def solution(begin, target, words):
    words.insert(0, begin)
    graph = defaultdict(list)
    
    for str1 in words:
        for str2 in words:
            if str1 == str2 or str2 == begin: 
                continue
            
            if diff(str1, str2):
                graph[str1].append(str2)            
    return bfs(begin, target, words, graph)


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))