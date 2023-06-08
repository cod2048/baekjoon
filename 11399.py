import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
# s_lst = sorted(lst)
# result = 0
# ans = 0

# for i in range(n):
#     result += s_lst[i]
#     ans += result

# print(ans)

s = [0]*n

for i in range(1, n):
    insert_point = i # 현재 인덱스 번호 저장
    insert_value = lst[i] # 현재 값 저장
    for j in range(i-1, -1, -1): # 현재 값 위치의 바로 전 값을 비교하면서 왼쪽으로 이동
        if lst[j] < lst[i]: # 비교대상이 나보다 작으면(해당 위치에 삽입해야함)
            insert_point = j+1 # 나보다 작은 값의 앞에 저장해야하니 +1
            break
        if j == 0: # 끝까지 탐색했을 경우(현재 값이 가장 작은 값일 경우)
            insert_point = 0 # 맨 앞에 삽입
    for j in range(i, insert_point, -1): # i부터 insert_point까지
        lst[j] = lst[j-1] # 값들을 오른쪽으로 한 칸씩 shift
    lst[insert_point] = insert_value # 삽입 위치에 현재 데이터 저장

s[0] = lst[0]

for i in range(1, n):
    s[i] = s[i-1] + lst[i] # 합 배열 공식

sum = 0

for i in range(0, n):
    sum += s[i]

print(sum)