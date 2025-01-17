def solution(n, m, section):
    answer = 0
    start = 0
    
    for sect in section:
        if sect > start:
            answer += 1
            start = sect + m - 1
            
    return answer