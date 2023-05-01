n = int(input())
score = list(map(int, input().split()))
result = []
m = max(score)

for i in range(n):
	x = score[i]/m*100
	result.append(x)
    
print(sum(result)/n)