x, y, w, h = map(int, input().split())

a = w-x
if a >= x:
    a = x
b = h-y
if b >= y:
    b = y

if a<=b:
    print(a)
else:
    print(b)