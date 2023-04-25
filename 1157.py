n = input()
word = n.lower()
word_list = list(set(word))
result = []

for i in word_list:
    cnt = word.count(i)
    result.append(cnt)

if result.count(max(result)) > 1:
    print('?')
else:
    print(word_list[(result.index(max(result)))].upper())