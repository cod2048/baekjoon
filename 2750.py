n = int(input())
lst = []
    
for i in range(n):
    x = int(input())
    lst.append(x)

for i in range(n-1):
    for j in range(n-1-i):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp

for i in range(n):
    print(lst[i])