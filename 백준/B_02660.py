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
            return visited[v]-1

        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v]+1


N = int(input())
G = [[] for _ in range(N+1)]        # 인접그래프
arr = [[0]*N for _ in range(N+1)]

while True:
    u, v = map(int,input().split())
    if u == -1 and v == -1:
        break
    G[u].append(v)
    G[v].append(u)

for i in range(1,N):
    for j in range(i+1,N+1):
        result = bfs(i,j)
        arr[i-1][j-1] = result
        arr[j-1][i-1] = result

rank = [0] * N

# for i in range(N):
#     print(*arr[i])

for i in range(N):
    rank[i] = max(arr[i])

tmp = min(rank)
answer = []
cnt = 0
for i in range(N):
    if rank[i] == tmp:
        cnt += 1
        answer.append(i+1)

print(tmp, cnt)
print(*answer)


