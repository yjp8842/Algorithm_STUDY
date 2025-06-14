def isCorrect(u):
    stack = []
    for el in u:
        if el == '(':
            stack.append(el)
        else:
            if not stack:
                return False
            
            stack.pop()
            
    return True

def solution(p):
    answer = ''
    u = []
    v = []
    open = 0
    close = 0
    
    if not p:
        return ''

    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    if isCorrect(u):
        return u + solution(v)
    
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        
        for el in u[1:-1]:
            if el == '(':
                answer += ')'
            else:
                answer += '('
                
    return answer