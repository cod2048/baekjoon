n = input()

count = 0

for i in range(1, int(n)+1):
    if (i<100):
        count += 1
    elif(i>=100):
        i = str(i)
        if (int(i[0])-int(i[1]))==(int(i[1])-int(i[2])):
            count +=1
    # else:
    #     

print(count)
        

