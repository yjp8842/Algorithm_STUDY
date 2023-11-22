import sys
input = sys.stdin.readline

N = int(input())
people = []
for _ in range(N):
  age, name = input().split()
  people.append([int(age), name])

sort_people = sorted(people, key=lambda x:x[0])

for person in sort_people:
  print(person[0], person[1])