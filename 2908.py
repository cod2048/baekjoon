import sys
input = sys.stdin.readline

A, B = map(str, input().split())

opposite_A = int(A[2]+A[1]+A[0])
opposite_B = int(B[2]+B[1]+B[0])

print(max(opposite_A, opposite_B))