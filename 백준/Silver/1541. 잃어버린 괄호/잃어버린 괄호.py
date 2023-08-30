# 먼저 '-'를 기준으로 문자열 자름
# '-'가 나오기 전 모든 값들을 더함
# '-'가 나온 후부터 해당 값들을 모두 빼줌

# 55-50+40 -> 55-(50+40) -> -35
# 55 / 50+40 -> 55 - 50 - 40 -> -35

str_s = input().split('-')

sums = 0
n_str = str_s[0].split('+')
for num in n_str:
  sums += int(num)
  
for strs in str_s[1:]:
  m_str = strs.split('+')
  for num in m_str:
    sums -= int(num)
    
print(sums)