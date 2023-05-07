l=[]
r=''
for i in range(5):
    l.append(input())
for i in range(15):
    for j in range(5):
        if len(l[j])>i:
            r+=l[j][i]
print(r)