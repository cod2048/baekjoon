c = int(input())

for i in range(c):
    stds = list(map(int, input().split()))
    avg = sum(stds[1:])/stds[0]
    h_stds = 0
    for j in stds[1:]:
        if j > avg:
            h_stds += 1
    result = ((h_stds/stds[0])*100)
    print(('%.3f' %result) + '%')
