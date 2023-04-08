n = int(input())
result = ''

for i in range(n):
    r, s = input().split()
    r = int(r)
    p = ''
    for j in range(len(s)):
        p += r*s[j]
    result += f"{p}\n"

print(result)