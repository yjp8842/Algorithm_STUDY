import math

def solution(fees, records):
    answer = []
    record_lst = []
    for record in records:
        record_lst.append(record.split())
    
    cars = {}
    times = {}
    for record in record_lst:
        if record[2] in 'IN':
            cars[record[1]] = record[0]
        else:
            in_hour = int(cars[record[1]].split(':')[0]) * 60
            in_minute = int(cars[record[1]].split(':')[1])
            out_hour = int(record[0].split(':')[0]) * 60
            out_minute = int(record[0].split(':')[1])
            if record[1] in times:
                times[record[1]] += ((out_hour + out_minute) - (in_hour + in_minute))
            else:
                times[record[1]] = ((out_hour + out_minute) - (in_hour + in_minute))
            
            del cars[record[1]]
    
    for record in record_lst:
        if record[1] in cars:
            in_hour = int(cars[record[1]].split(':')[0]) * 60
            in_minute = int(cars[record[1]].split(':')[1])
            out_hour = 23 * 60
            out_minute = 59
            if record[1] in times:
                times[record[1]] += ((out_hour + out_minute) - (in_hour + in_minute))
            else:
                times[record[1]] = ((out_hour + out_minute) - (in_hour + in_minute))
            
            del cars[record[1]]
    
    times = sorted(times.items())
    
    for time in times:
        if time[1] > fees[0]:
            answer.append(fees[1] + math.ceil((time[1] - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    
    return answer