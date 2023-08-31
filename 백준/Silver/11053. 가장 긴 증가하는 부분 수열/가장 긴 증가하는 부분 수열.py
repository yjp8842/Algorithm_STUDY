N = int(input())
arr = list(map(int, input().split()))

lists = [0] * N
for i in range(N):
  for j in range(i):
    # 이전의 숫자보다 크고
    # 횟수를 담은 이전의 값보다 작을 때
    if arr[i] > arr[j] and lists[i] < lists[j]:
      # 현재 횟수를 그 값으로 갱신
      lists[i] = lists[j]
  lists[i] += 1

# print(lists)
print(max(lists))