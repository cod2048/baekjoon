import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n

for i in range(n):  # range 범위 설정 오류 수정
    a[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    su = a[i]
    if su >= num:
        while su >= num:  # 변수명 오류 수정
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n_pop = stack.pop()  # 변수명 오타 수정
        if n_pop > su:
            print("NO")  # 대문자로 수정
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)
