import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(board)