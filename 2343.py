import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start = max(arr)
    end = sum(arr)
    while start <= end:
        mid = (start+end) // 2
        cnt = 0
        total = 0
        for i in range(len(arr)):
            if total + arr[i] > mid:
                cnt += 1
                total = 0
            total += arr[i]
        if total != 0:
            cnt += 1
        if cnt > target:
            start = mid +1
        else:
            end = mid -1
    return start

n, m = map(int, input().split())

lesson = list(map(int, input().split()))

print(binary_search(lesson, m))