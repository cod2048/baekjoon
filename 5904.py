import sys
input = sys.stdin.readline

n = int(input())

def moo_length(k):
    if k == 0:
        return 3
    else:
        return moo_length(k-1) + k + 3
