def solution(s):
    x = 0
    lst_s = [i for i in s]
    
    for _ in range(len(lst_s)):
        lst_s.append(lst_s.pop(0))
        check = []
        flag = len(lst_s)
        
        for strs in lst_s:
            flag -= 1
            if strs == "[" or strs == "(" or strs == "{":
                check.append(strs)

            elif strs == "]":
                if len(check) == 0 or check.pop() != "[":
                    flag = -1
                    break
            elif strs == ")":
                if len(check) == 0 or check.pop() != "(":
                    flag = -1
                    break
            elif strs == "}":
                if len(check) == 0 or check.pop() != "{":
                    flag = -1
                    break
                    
        if flag == 0 and len(check) == 0:
            x += 1
            
    return x