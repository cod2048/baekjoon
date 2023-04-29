n = int(input())

count = 0

for i in range(n):
    x = input()
    dic = {x[0]:1}
    flag = True
    for s in range(1,len(x)) :
        if x[s] not in dic.keys() :
            dic[x[s]] = 1
        else :
            if x[s-1] != x[s] :
                flag = False
                break
    if flag:
        count += 1
print(count)
        