import sys
from collections import deque
sys.stdin = open('B_02479.txt')

# 해밍 거리 그래프 만들기(무방향)
def haming():
    # 해밍 거리 인지 판단
    for i in range(1,N):
        for j in range(i+1,N+1):
            dist = 0
            for k in range(K):
                if arr[i][k] != arr[j][k]:
                    dist += 1
                    if dist > 1:
                        break
            if dist == 1:
                G[i].append(j)
                G[j].append(i)

# 그래프 탐색
def bfs(start):
    q = deque()
    q.append((start,[start]))
    visited = [0] * (N+1)
    visited[start] = 1

    while q:
        v,path = q.popleft()
        # print(v)
        # print(path)
        if v == end:
            return path
        for w in G[v]:
            if not visited[w]:
                q.append((w, path+[w]))
                visited[w] = 1

    return [-1]

N, K = map(int,input().split())
G = [[] for _ in range(N+1)]        # 그래프
arr = [0] * (N+1)
for i in range(1,N+1):
    arr[i] = input()

start, end = map(int,input().split())


haming()
result = bfs(start)

print(*result)