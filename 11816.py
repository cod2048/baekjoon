import sys
input = sys.stdin.readline

X = str(input().strip())
result = 0

if X[0] == '0':
  if X[1] == 'x':
    #16진수->10진수로 변환
    for i in range(len(X)-2):
      if ord(X[-(i+1)]) < 70:
        result += (16**i) * (ord(X[-(i+1)])-48)
      else:
        result += (16**i) * (ord(X[-(i+1)])-87)
    print(result)
  else:
    #8진수->10진수로 변환
    for i in range(len(X)-1):
      result += (8**i) * int(X[-(i+1)])
    print(result)
else:
  print(int(X))