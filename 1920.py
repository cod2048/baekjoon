import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

a.sort()

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return 0

for i in range(m):
    print(binary_search(a, num[i]))