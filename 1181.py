import sys
input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
  words.add(input().strip())

word_list = list(words)
word_list.sort()
word_list.sort(key=len)
for i in range(len(word_list)):
  print(word_list[i])