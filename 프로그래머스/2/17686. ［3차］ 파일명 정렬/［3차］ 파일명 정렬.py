def solution(files):
    answer = []

    for file in files:
        head, number, tail = '', '', ''
        check = False
        
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                check = True
            elif not check:
                head += file[i]
            else:
                tail = file[i:]
                break

        answer.append((head, number, tail))

    answer.sort(key=lambda x : (x[0].lower(), int(x[1])))
    answer = [''.join(value) for value in answer]
    
    return answer