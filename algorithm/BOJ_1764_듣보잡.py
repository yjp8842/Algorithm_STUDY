from sys import stdin

N, M = map(int, stdin.readline().split())
l_list = [stdin.readline() for _ in range(N)]
s_list = [stdin.readline() for _ in range(M)]

# set과 &를 활용하여 교집합 구하기
ls_list = list(set(l_list) & set(s_list))

print(len(ls_list))
for name in sorted(ls_list):
    # 개행 문자가 들어가 있어서 출력 형식에 맞게 바꿔줌
    print(name, end="")