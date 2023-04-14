import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
    
a.sort()
    
def find_num(lst, key):
    left_key = 0
    right_key = len(lst)-1
    while True:
        mid_num = (left_key+right_key) // 2
        if lst[mid_num] == key:
            return 1
        elif lst[mid_num] < key:
            left_key = mid_num + 1
        else:
            right_key = mid_num - 1
        if left_key > right_key:
            return 0
        

for i in range(len(b)):
    print(find_num(a, b[i]))