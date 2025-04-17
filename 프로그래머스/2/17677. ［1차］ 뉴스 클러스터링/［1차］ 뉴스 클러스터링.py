def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    set_str1 = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            set_str1.append(str1[i:i + 2])

    set_str2 = []
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            set_str2.append(str2[i:i + 2])

    intersection = []
    sums = len(set_str1) + len(set_str2)
    
    if len(set_str1) < len(set_str2):
        for i in range(len(set_str1)):
            if set_str1[i] in set_str2:
                intersection.append(set_str1[i])
                set_str2.pop(set_str2.index(set_str1[i]))
    else :
        for i in range(len(set_str2)):
            if set_str2[i] in set_str1:
                intersection.append(set_str2[i])
                set_str1.pop(set_str1.index(set_str2[i]))

    union = sums - len(intersection)

    if sums == 0:
        return 65536
    else:
        return int((len(intersection) / union) * 65536)