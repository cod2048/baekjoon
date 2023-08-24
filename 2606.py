# n = int(input())
# m = int(input())
# graph = [[]*n for _ in range(n+1)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# cnt = 0
# visited = [0]*(n+1)
# def dfs(start):
#     global cnt
#     visited[start] = 1
#     for i in graph[start]:
#         if visited[i]==0:
#             dfs(i)
#             cnt +=1
 
# dfs(1)
# print(cnt)

import sys
from collections import deque
input = sys.stdin.readline

#### 입력 값 받기 #############################################
computer = int(input())
network = int(input())
graph = [[] for _ in range(computer + 1)]
for _ in range(network):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


#### 필요한 변수 선언 ##########################################
visited = [False] * (computer + 1)

# BFS 함수 구현 ##############################################
def bfs(lst, target) :
    count = 0
    ## 초기 큐 세팅############
    queue = deque()
    queue.append(target)
    visited[target] = True
    
    ## 탐색 ###################
    while queue:
        ctarget = queue.popleft()
        for i in range(len(lst[ctarget])) :
            if visited[lst[ctarget][i]] == False:
                count += 1
                visited[lst[ctarget][i]] = True
                queue.append(lst[ctarget][i])
    print(count)

# 그래프 탐색 - 따지고 보면 main ##########################

bfs(graph, 1)

# 출력 ###############################################