import sys
input = sys.stdin.readline

def append_star(length):
    if length == 1:
        return ['*']

    stars = append_star(length//3) 
    l = []  
    
    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s+' '*(length//3)+s)
    for s in stars:
        l.append(s*3)
    return l

n = int(input().strip())
print('\n'.join(append_star(n)))