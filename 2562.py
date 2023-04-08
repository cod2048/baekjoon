a = []

for i in range(0, 9):
    a.append(int(input()))

x = a[0]
b = 0
for i in range(0,9):
    if i == 0:
        x= a[0]
        b= 1

    if x < a[i]:
        x = a[i]
        b = i+1

print(x)
print(b)