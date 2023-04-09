import math

a, b, v = input().split()
a = int(a)
b = int(b)
v = int(v)


print(math.ceil((v-b)/(a-b)))