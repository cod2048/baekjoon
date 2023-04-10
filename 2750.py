n = int(input())
list = []
    
for i in range(n):
    x = int(input())
    list.append(x)

list.sort()

for i in list:
    print(i)