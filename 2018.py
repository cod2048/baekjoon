import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
sum = 1
start_index = 1
end_index = 1

while end_index != n:
    if sum < n:
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        cnt += 1
        end_index += 1
        sum += end_index

print(cnt)