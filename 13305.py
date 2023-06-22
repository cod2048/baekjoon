import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = road[0] * price[0]
    
min_cost = price[0]
    
for i in range(1, n-1):
    if min_cost > price[i]:
        min_cost = price[i]
    
    min_price += min_cost * road[i]

print(min_price)
