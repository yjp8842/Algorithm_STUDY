from itertools import combinations

N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

house_list = []
chicken_list = []
for i in range(N):
  for j in range(N):
    if cities[i][j] == 1:
      # 집의 좌표 값을 담을 리스트에 append
      house_list.append((i, j))
    elif cities[i][j] == 2:
      # 가게의 좌표 값을 담을 리스트에 append
      chicken_list.append((i, j))

# 도시의 치킨 거리 최단거리 찾아주는 함수 
def check_distance(house_list, stores):
  sum_dist = 0
  dist = 0
  for r, c in house_list:
    # 최소값을 구하기 위해 엄청 큰 양수로 초기화
    min_dist = 1e9
    for a, b in stores:
      dist = abs(r - a) + abs(c - b)
      # 계속해서 최솟값 갱신해주기
      min_dist = min(dist, min_dist)
    # 한 집의 최단거리 계산 끝날 때마다 sum_dist 변수에 해당 거리 더해주기
    sum_dist += min_dist
  return sum_dist

result = 1e9
# M개의 가게를 고르는 조합 함수 이용
for lists in combinations(chicken_list, M):
  # 각각 리스트를 check_distance 함수에 넣어 최솟값 갱신해주기
  result = min(result, check_distance(house_list, lists))

print(result)