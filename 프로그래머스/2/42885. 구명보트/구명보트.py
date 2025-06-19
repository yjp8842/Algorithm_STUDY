def solution(people, limit):
    answer = 0
    start, end = 0, len(people) - 1
    people.sort()
    
    while True:
        if start > end:
            break
        
        if people[start] + people[end] > limit:
            end -= 1
        else:
            start += 1
            end -= 1

        answer += 1
    
    return answer