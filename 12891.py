import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input()
min_dna = list(map(int, input().split()))
check_dna = [0] * 4
check = 0
cnt = 0

def dna_add(x):
    global check_dna, check, min_dna
    if x == 'A':
        check_dna[0] += 1
        if check_dna[0] == min_dna[0]:
            check += 1
    elif x == 'C':
        check_dna[1] += 1
        if check_dna[1] == min_dna[1]:
            check += 1
    elif x == 'G':
        check_dna[2] += 1
        if check_dna[2] == min_dna[2]:
            check += 1
    elif x == 'T':
        check_dna[3] += 1
        if check_dna[3] == min_dna[3]:
            check += 1

def dna_remove(x):
    global check_dna, check, min_dna
    if x == 'A':
        if check_dna[0] == min_dna[0]:
            check -= 1
        check_dna[0] -= 1
    elif x == 'C':
        if check_dna[1] == min_dna[1]:
            check -= 1
        check_dna[1] -= 1
    elif x == 'G':
        if check_dna[2] == min_dna[2]:
            check -= 1
        check_dna[2] -= 1
    elif x == 'T':
        if check_dna[3] == min_dna[3]:
            check -= 1
        check_dna[3] -= 1

for i in range(4):
    if min_dna[i] == 0:
        check += 1
    
for i in range(p):
    dna_add(dna[i])

if check == 4:
    cnt += 1

for i in range(p, s):
    j = i - p
    dna_add(dna[i])
    dna_remove(dna[j])
    if check == 4:
        cnt += 1

print(cnt)