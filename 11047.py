import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
coins_list = deque()
for _ in range(n):
    coin = int(input())
    coins_list.appendleft(coin)

def make_money(coins, result):
    cnt = 0
    for coin in coins:
        while coin <= result:
            cnt += 1
            result -= coin
    return cnt
    
print(make_money(coins_list, k))