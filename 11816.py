import sys
input = sys.stdin.readline

x = str(input())


if x[0] == '0' and x[1] != 'x':
    print(int(x[1:], 8))
elif x[0] == '0' and x[1] == 'x':
    print(int(x[2:], 16))
else:
    print(int(x))

