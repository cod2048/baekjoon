import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}

for i in range(n):
    word = input().strip()
    if len(word) >= m:
        if word in words:
            words[word] = words[word] +1
            continue
        words[word] = 1

words = dict(sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0])))

for i in words.keys():
    print(i)