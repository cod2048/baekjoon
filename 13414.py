import sys
input = sys.stdin.readline

k, l = map(int, input().split())
students = {}
for i in range(l):
    student = input().strip()
    students[student] = i

students = sorted(students.items(), key = lambda x: (x[1]))

cnt = 0

for i in range(len(students)):
    cnt += 1
    print(students[i][0])
    if cnt == k:
        break