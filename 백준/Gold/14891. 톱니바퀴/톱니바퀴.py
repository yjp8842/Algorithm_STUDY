from collections import deque


lists = []
for _ in range(4):
  queue = deque(list(map(int, input())))
  lists.append(queue)
K = int(input())
rotate = []
for _ in range(K):
  rotate.append(list(map(int, input().split())))

# 회전해야 하는지 체크하는 함수
def check(idx, direct):
  # 돌아가야 하는지 아닌지 확인하는 리스트
  is_rotate = [0 for _ in range(4)]
  is_rotate[idx] = 1
  
  # 오른쪽 톱니바퀴 검사
  for i in range(idx - 1, -1, -1):
    if lists[i][2] != lists[i + 1][6]:
      is_rotate[i] = 1
    else:
      break
  
  # 왼쪽 톱니바퀴 검사
  for i in range(idx + 1, 4):
    if lists[i][6] != lists[i - 1][2]:
      is_rotate[i] = 1
    else:
      break
  
  # 돌아가야 하는 톱니바퀴가 시계 방향인지 반시계 방향인지 확인하며 함수 진행
  for i in range(4):
    if is_rotate[i] == 1:
      if idx == 0 or idx == 2:
        if i == 0 or i == 2:
          rotate_wheel(i, direct)
        else:
          rotate_wheel(i, -direct)
      if idx == 1 or idx == 3:
        if i == 1 or i == 3:
          rotate_wheel(i, direct)
        else:
          rotate_wheel(i, -direct)


# 톱니바퀴 회전하는 함수
def rotate_wheel(num, direct):
  # 시계 방향일 때
  if direct == 1:
    # 맨 끝에 것을 빼서 맨 앞으로 옮겨주기
    lists[num].appendleft(lists[num].pop())
    # lists[num][0] = lists[num][7]
    # for i in range(1, 8):
    #   lists[num][i] = lists[num][i - 1]
      
  # 반시계 방향일 때
  else:
    # 맨 앞에 있는 것을 빼서 맨 끝으로 옮겨주기
    lists[num].append(lists[num].popleft())
    # lists[num][7] = lists[num][0]
    # for i in range(7):
    #   lists[num][i] = lists[num][i + 1]


for i in range(K):
  # 인덱스로 접근하기 때문에 -1 해줘야함
  wheel = rotate[i][0] - 1
  
  # 시계 방향
  if rotate[i][1] == 1:
    check(wheel, 1)
  else:
    check(wheel, -1)

ans = 0
if lists[0][0] == 1:
	ans += 1
if lists[1][0] == 1:
	ans += 2
if lists[2][0] == 1:
	ans += 4
if lists[3][0] == 1:
	ans += 8

print(ans)