import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_num = set(map(int, input().split()))
b_num = set(map(int, input().split()))

union_num = a_num | b_num
intersection_num = a_num & b_num

print(len(union_num - intersection_num))