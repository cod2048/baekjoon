import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
  test_case = list(map(int, input().split()))
  student_num = test_case[0]
  average_score = sum(test_case[1:]) / student_num
  result = 0
  for i in test_case[1:]:
    if i > average_score:
      result += 1
  print(str(format(result / student_num * 100, ".3f"))+'%')