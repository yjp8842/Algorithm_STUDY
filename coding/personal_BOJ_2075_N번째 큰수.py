""" # 버블 정렬 함수 정의하기
def bubble_sort(a, N):
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                
N = int(input())
num_list = []
# 2차원 리스트 input 받기
for i in range(N):
    input_list = list(map(int, input().split()))
    num_list.append(input_list)

# 2차원 리스트를 1차원 리스트로 변환하기
result_list = []
for inner_list in num_list:
    for data in inner_list:
        result_list.append(data)

        # 오름차순으로 정렬
        M = len(result_list)
        for i in result_list:
            bubble_sort(result_list, M)

# 마지막에서 N번째 값    
print(result_list[M - N]) """

# 메모리 초과..
# heap은 기본값 = 최소힙
# 트리의 루트에 가장 작은 값이 위치
# N개의 최댓값을 뽑아내야함
# *주의* 내림차순, 오름차순으로 정렬되는 것이 아님
import heapq

N = int(input())
num_list = []
for _ in range(N):
    nums = list(map(int, input().split()))
    
    for i in nums:
        # num_list의 길이가 N을 넘어가지 않도록
        # N이 5이면, num_list에는 5개의 숫자만 담기도록
        if len(num_list) < N:
            heapq.heappush(num_list, i)
        # N을 넘어가면 업데이트
        else:
            # num_list에 담겨 있는 숫자 중 가장 작은값 즉, num_list[0] 보다 클때만
            if i > num_list[0]:
                heapq.heapreplace(num_list, i) # num_list의 가장 작은 데이터 추출하고 i 삽입
                
    # num_list에는 입력받은 숫자 중 가장 큰 값 N개가 들어있게 됨
                
print(num_list[0])