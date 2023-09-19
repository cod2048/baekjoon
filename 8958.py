import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
  answer = input()
  score = 0
  result = 0
  for i in range(len(answer)):
    if answer[i] == 'O':
      score += 1
      result += score
    else:
      score = 0
      continue
  print(result)