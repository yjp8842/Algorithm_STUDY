def solution(cacheSize, cities):
    cache = []
    times = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in cities:
        city = i.upper()
        
        if city in cache:
            cache.remove(city)
            cache.append(city)
            times += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
                cache.append(city)
                times += 5
            else:
                cache.append(city)
                times += 5
        
    return times