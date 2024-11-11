import sys
sys.stdin = open('B_01916.txt')
from heapq import heappush,heappop

def dijkstra(start, end):
    visited = [0] * (V+1)   # 비용이 결정된 노드
    D[start] = 0
    hq = [(0,start)]

    cnt = V

    while cnt and hq:
        w, v = heappop(hq)

        if visited[v]:
            continue
        if v == end:
            print(D[v])
            return
        visited[v] = 1
        for u,weight in G[v]:
            if not visited[u] and D[u] > D[v] + weight:
                D[u] = D[v] + weight
                heappush(hq,(D[u], u))
        cnt -= 1

V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    G[u].append((v,w))

start, end = map(int,input().split())

D = [float('inf')] * (V+1)

dijkstra(start,end)
