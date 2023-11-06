def solution(priorities, location):
    answer = 0
    
    place = priorities.index(max(priorities))
    while (True):
        value = max(priorities)
    
        if (priorities[place] == value):
            priorities[place] = 0
            answer += 1
            
            if (place == location):
                break

        place += 1
        if (place >= len(priorities)):
            place = 0
            
    return answer