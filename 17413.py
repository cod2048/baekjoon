import sys
S = sys.stdin.readline().strip()
ans = ''
word = ''
tag = 0
for a in S:
    if a == ' ' and tag == 0:
        ans+=word[::-1]
        ans+=' '
        word = ''
    elif a=='<':
        ans+=word[::-1]
        word = '<'
        tag = 1
    else:
        word += a
        if a == '>':
            ans+=word
            word = ''
            tag = 0
if word:
    ans+=word[::-1]
print(ans)