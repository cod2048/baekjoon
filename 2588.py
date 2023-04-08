a = int(input())
b = input()

c = (a*int(b[-1]))
d = (a*int(b[-2]))
e = (a*int(b[-3]))
f = c + (d*10) + (e*100)

print(c)
print(d)
print(e)
print(f)