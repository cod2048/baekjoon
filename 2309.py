dwarfs = []

for i in range(9):
    x = int(input())
    dwarfs.append(x)

total = sum(dwarfs)
one = 0
two = 0

for i in range(9):
    for j in range(i+1, 9):
        if total-(dwarfs[i] + dwarfs[j]) == 100:
            one, two = dwarfs[i], dwarfs[j]
            break

dwarfs.remove(one)
dwarfs.remove(two)
    
dwarfs.sort()

for i in range(len(dwarfs)):
    print(dwarfs[i])