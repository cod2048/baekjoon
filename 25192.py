import sys
input = sys.stdin.readline

n = int(input().strip())

chatLog = set()
cnt = 0

for i in range(n):
    chat = input().strip()
    if chat != "ENTER":
        chatLog.add(chat)
    else:
        cnt += len(chatLog)
        chatLog = set()

cnt += len(chatLog)

print(cnt)