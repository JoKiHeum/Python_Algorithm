import sys
sys.stdin = open('B_02660.txt')

from collections import deque

def bfs(start,end):
    q = deque()
    q.append(start)
    visited = [0] * (N+1)
    visited[start] = 1

    while q:
        v = q.popleft()
        if v == end:
            print(start,end)
            return visited[v]-1

        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v]+1


N = int(input())
G = [[] for _ in range(N+1)]        # 인접그래프
arr = [[0]*N for _ in range(N+1)]

for _ in range(N):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1,N):
    for j in range(i+1,N+1):
        result = bfs(i,j)
        arr[i-1][j-1] = result
        arr[j-1][i-1] = result

for i in range(N):
    print(*arr[i])
