import sys
input = sys.stdin.readline # input 함수 재정의
from heapq import heappop,heappush

def dijkstra(start):
    visited = [0] * (V+1)
    D[start] = 0
    hq = [(0,start)]

    cnt = V
    while cnt and hq:
        w,v = heappop(hq)

        if visited[v]:
            continue

        visited[v] = 1
        for u, weight in G[v]:
            if D[u] > D[v] + weight:
                D[u] = D[v] + weight
                heappush(hq,(D[u],u))
        cnt -= 1

V, E = map(int,input().split())
K = int(input())
G = [[] for _ in range(V+1)]
D = [float('inf')] * (V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    G[u].append((v,w))

dijkstra(K)
for i in range(1,V+1):
    if D[i] == float('inf'):
        print('INF')
    else:
        print(D[i])