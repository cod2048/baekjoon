word = input()

for i in range(1, len(word)):
    if word[i-1] == word[-i]:
        continue
    else:
        print(0)
        break
else:
    print(1)
    
