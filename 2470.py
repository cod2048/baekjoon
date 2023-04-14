# n = int(input())
# liquid = sorted(list(map(int, input().split())))

# # 초기 최솟값 설정
# min_val = 10000000
# a = 0
# b = 0

# def find_min(start, end):
#     global min_val, a, b  # 전역 변수로 사용
#     if start >= end:  # start와 end 인덱스가 범위를 벗어난 경우 종료
#         return
#     # 처음 값과 마지막 값의 차이 저장
#     diff = abs(abs(liquid[start]) - abs(liquid[end]))
#     # 초기 최솟값과 계산값 비교
#     if diff < min_val:
#         # 최솟값 저장
#         a = liquid[start]
#         b = liquid[end]
#         min_val = diff
#     # 다음 인덱스로 이동하여 재귀적으로 호출
#     if abs(liquid[start+1]) < abs(liquid[end-1]):
#         find_min(start+1, end)
#     else:
#         find_min(start, end-1)

# find_min(0, n-1)
# print(a, b)

import sys

n = int(input())
liquid = sorted(list(map(int, input().split())))

min_val = sys.maxsize
a, b = 0, 0

start = 0
end = n-1

while start < end:
    diff = liquid[start] + liquid[end]
    if abs(diff) < min_val:
        a = liquid[start]
        b = liquid[end]
        min_val = abs(diff)
        if min_val == 0:
            break
    if diff < 0:
        start += 1
    else:
        end -= 1

print(a, b)
