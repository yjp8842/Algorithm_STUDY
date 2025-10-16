def solution(record):
    answer = []
    records = []
    for r in record:
        records.append(r.split())
    
    names = {}
    messages = []
    for i in range(len(records)):
        if records[i][0] == 'Enter':
            command, user_id, nickname = records[i]
            messages.append([command, user_id])
            names[user_id] = nickname
        elif records[i][0] == 'Change':
            command, user_id, nickname = records[i]
            names[user_id] = nickname
        else:
            command, user_id = records[i]
            messages.append([command, user_id])
    
    for i in range(len(messages)):
        if messages[i][0] == 'Enter':
            answer.append(names[messages[i][1]] + '님이 들어왔습니다.')
        else:
            answer.append(names[messages[i][1]] + '님이 나갔습니다.')

    return answer