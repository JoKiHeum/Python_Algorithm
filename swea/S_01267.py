import sys
sys.stdin = open('S_01267.txt')
from collections import deque

def topology_sort():
    q = deque()

    for i in range(1, V+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        v = q.popleft()
        print(v, end=' ')

        for w in G[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                q.append(w)


for test_case in range(1,2):
    V, E = map(int, input().split())        # V: 정점의 갯수, E: 간선의 수
    edges = list(map(int, input().split())) # 간선 정보
    G = [[] for _ in range(V+1)]            # 인접리스트
    indegree = [0] * (V+1)
    for i in range(E):
        u, v = edges[i*2] ,edges[i*2+1]
        G[u].append(v)
        indegree[v] +=1

    print(indegree)


    print(f'#{test_case}', end=' ')
    topology_sort()
    print()

