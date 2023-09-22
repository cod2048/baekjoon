import sys
input = sys.stdin.readline

N = int(input())
queue = [None] * N
start = 0
end = 0

for _ in range(N):
  order = list(map(str, input().split()))
  if order[0] == "push":
    queue[end] = order[1]
    end += 1
  elif order[0] == "pop":
    if end-start:
      print(queue[start])
      queue[start] == None
      start += 1
    else:
      print(-1)
  elif order[0] == "size":
    print(end-start)
  elif order[0] == "empty":
    if end-start:
      print(0)
    else:
      print(1)
  elif order[0] == "front":
    if end-start:
      print(queue[start])
    else:
      print(-1)
  elif order[0] == "back":
    if end-start:
      print(queue[end-1])
    else:
      print(-1)

# push X : 정수 X를 큐에 넣음
# pop : 가장 앞에 있는 정수를 빼고 출력,수가 없으면 -1
# size : 큐에 들어있는 정수의 개수 출력
# empty : 큐가 비어있으면 1, 아니면 0
# front : 큐의 가장 앞에 있는 정수를 출력, 정수가 없으면 -1
# back : 큐의 가장 뒤에 있는 정수를 출력, 정수가 없으면 -1