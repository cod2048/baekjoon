import sys
input = sys.stdin.readline
x = int(input().strip())

a = 1
b = 2

while a<x:
    a+=b
    b+=1

n = a-x+1

if b%2 == 1:
    b-=n    
    print(f"{b}/{n}")
else:
    b-=n
    print(f"{n}/{b}")

# 원주가 내 코드 따라함;;