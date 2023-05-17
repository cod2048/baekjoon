n, m, k = map(int, input().split())

def comb(n, k):
    p = 1
    c = 1
    while(k>0):
        c *= n
        p *= k
        n -= 1
        k -= 1
    return c/p


result = 0.0
p = comb(n, m)

while(m>=k):
    if(n-m) < (m-k):
        k += 1
        continue
    c = comb(m, k) * comb(n-m, m-k);
    result += c/p
    k += 1

print(result)
