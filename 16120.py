import sys
input = sys.stdin.readline

n = input().strip()
ppap = []
for i in range(len(n)):
	ppap.append(n[i])
	if ppap[-1] == 'P' and ppap[-4: ] == list('PPAP'):
		del ppap[-3: ]
 
if ppap == list('P'):
	print('PPAP')
else:
	print('NP')