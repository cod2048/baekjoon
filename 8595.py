import sys
input = sys.stdin.readline

n = int(input())
words = input().strip()

result = 0
number = ''

for word in words:
    if ord('0') <= ord(word) <= ord('9'):
        number += word
    else:
        if number == '':
            continue
        result += int(number)
        number = ''

if number != '':
    result += int(number)

print(result)