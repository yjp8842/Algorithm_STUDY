def solution(elements):
    lst = []
    len_el = len(elements)
    for i in range(1, len_el + 1) :
        for j in range(len_el) :
            if j + i > len_el :
                lst.append(sum(elements[j:]) + sum(elements[:j + i - len_el]))
            else :
                lst.append(sum(elements[j:j + i]))
    
    set_lst = set(lst)
    result = len(list(set_lst))
    
    return result