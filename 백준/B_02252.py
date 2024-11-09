import sys
sys.stdin = open('B_02252.txt')
from collections import deque

def topology_sort():
    q = deque()

    for i in range(1,N+1):
        if indgree[i] == 0:
            q.append(i)

    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in G[v]:
            indgree[w] -= 1

            if indgree[w] == 0:
                q.append(w)



N, M = map(int, input().split())
G = [[] for _ in range(N+1)]        # 인접리스트
indgree = [0] * (N+1)

for i in range(M):
    v,w = map(int, input().split())
    G[v].append(w)
    indgree[w] += 1



topology_sort()