def solution(survey, choices):
    char = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        if choices[i] == 1:
            char[survey[i][0]] += 3
        elif choices[i] == 2:
            char[survey[i][0]] += 2
        elif choices[i] == 3:
            char[survey[i][0]] += 1
        elif choices[i] == 5:
            char[survey[i][1]] += 1
        elif choices[i] == 6:
            char[survey[i][1]] += 2
        elif choices[i] == 7:
            char[survey[i][1]] += 3
        else:
            continue
    
    # 키 값들만 뽑아서 리스트로 반환
    char_keys = list(char.keys())
    
    answer = ''
    for i in range(0, len(char), 2):
        # 두 개씩 묶어서 더 큰 값 검사하기
        if char[char_keys[i]] >= char[char_keys[i + 1]]:
            answer += char_keys[i]
        elif char[char_keys[i]] < char[char_keys[i + 1]]:
            answer += char_keys[i + 1]  
    
    return answer