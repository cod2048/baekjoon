import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, N+1):
    if (i<100):
        cnt += 1
    else:
        i = str(i)
        if (int(i[0])-int(i[1]))==(int(i[1])-int(i[2])):
            cnt +=1 

print(cnt)
        

