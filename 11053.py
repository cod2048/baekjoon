n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(len(arr)):
    for j in(i, len(arr)):
        if arr[i] > arr[j]:
            arr.remove(arr[i+1])

print(len(arr))