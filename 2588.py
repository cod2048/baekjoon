import sys
input = sys.stdin.readline

a = int(input())
b = str(input().strip())

first_line = int(b[-1])*a
second_line = int(b[-2])*a
third_line = int(b[-3])*a

result = first_line + second_line*10 + third_line*100

print(first_line)
print(second_line)
print(third_line)
print(result)