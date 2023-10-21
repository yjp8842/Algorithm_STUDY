def solution(s):
    answer = -1
    arr = list(map(str, s.strip()))
    result = []
    result.append(arr[0])
    for i in range(1, len(arr)):
        if len(result) > 0:
            if result[-1] == arr[i]:
                result.pop()
            else:
                result.append(arr[i])
        else:
            result.append(arr[i])
    
    if len(result) == 0:
        return 1
    else:
        return 0

    return result