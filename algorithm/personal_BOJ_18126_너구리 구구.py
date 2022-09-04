""" N = int(input())
arr = []
for _ in range(N - 1):
    arr.append(list(map(int, input().split())))

rooms = [[] for _ in range(N + 1)]
road_len = [[] for _ in range(N + 1)]
for i in range(len(arr)):
    rooms[arr[i][0]].append(arr[i][1])
    road_len[arr[i][1]].append(arr[i][2])

cnt = 0    
for i in rooms[1]:
    cnt += road_len[i][0]
    if rooms[i]:
        j = max(rooms[i])
        cnt += road_len[j][0]
        
print(cnt) """

""" N = int(input())
arr = []
for _ in range(N - 1):
    arr.append(list(map(int, input().split())))

rooms = [[] for _ in range(N + 1)]
road_len = [[] for _ in range(N + 1)]
for i in range(len(arr)):
    rooms[arr[i][0]].append(arr[i][1])
    road_len[arr[i][1]].append(arr[i][2])

cnt_list = [] 
for i in rooms[1]:
    cnt1 = 0
    cnt1 = road_len[i][0]
    for j in rooms[i]:
        cnt2 = 0
        cnt2 = road_len[j][0]
        cnt_list.append(cnt1 + cnt2)
       
print(cnt_list) """

# 모르겠어... to be continue...