n = int(input())
result = list(map(int, input().split()))
sum = 0

for i in range(n):
    aver = float(result[i]/max(result)*100)
    sum += aver

print(sum/n)
