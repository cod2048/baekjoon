n = int(input())

chatLog = set()
cnt = 0

for i in range(n):
    chat = input()
    if chat != "ENTER":
        chatLog.add(chat)
    else:
        cnt += len(chatLog)
        chatLog = set()

cnt += len(chatLog)

print(cnt)