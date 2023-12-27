N = int(input())
scores = list(map(int, input().split()))

new_scores = sorted(scores)

answer = 0
for score in new_scores:
  answer += score / new_scores[-1] * 100
  
print(answer / N)