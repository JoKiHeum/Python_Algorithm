import sys
sys.stdin = open('S_01248.txt')

# DFS를 활용한 길 찾기
def bfs(v,path,target):







T = int(input())
for test_case in range(1,T+1):
    V, E, X, Y = map(int,input().split())       # V: 정점의 수, E: 간선의 수, X,Y: 공통조상을 찾는 두 정점
    edges = list(map(int,input().split()))
    tree = [[] for _ in range(V+1)]

    for i in range(E):
        u, v = edges[i*2], edges[i*2+1]
        tree[u].append(v)

    visited = [0] * (V+1)
