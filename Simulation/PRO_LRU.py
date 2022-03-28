#######Example
cacheSize = 3
reference = [4, 2, 3, 4, 5, 6, 5, 4, 7]
cache = []
for ref in reference:
    if not ref in cache:
        if len(cache) < cacheSize:
            cache.append(ref)
        else:
            cache.pop(0)
            cache.append(ref)
    else:
        cache.pop(cache.index(ref))
        cache.append(ref)

########Programmers
def solution(cacheSize, cities):
    cache = []
    answer = 0

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)

        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)

    return answer


##### 다른 사람 코드
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen = cacheSize)
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5
    return time

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))