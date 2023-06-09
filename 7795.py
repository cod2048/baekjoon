T = int(input())
 
def binary_search(target,data):
    start = 0
    end = len(data) - 1
    res = -1
    while start <= end :
        mid = (start + end) // 2
        if data[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res
 
for _ in range(T):
    a,b = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    count = 0
 
    for i in A:
        count += binary_search(i,B) + 1
 
    print(count)
