def solution(skill, skill_trees):
    cnt = 0
    
    for skills in skill_trees:
        lst = []
        for s in skills:
            if s in skill:
                lst.append(s)
        
        for i in range(len(lst)):
            if lst[i] != skill[i]:
                cnt += 1
                break
                
    answer = len(skill_trees) - cnt
    
    return answer
