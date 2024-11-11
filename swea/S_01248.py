import sys
sys.stdin = open('S_01248.txt')

# DFS를 활용한 길 찾기
def dfs(v,path,target):
    global global_path
    visited[v] = 1
    path.append(v)
    if v == target:
        global_path = path[:]

    for w in tree[v]:
        if not visited[w]:
            dfs(w,path,target)
            path.pop()

T = int(input())
for test_case in range(1,2):
    V, E, X, Y = map(int,input().split())       # V: 정점의 수, E: 간선의 수, X,Y: 공통조상을 찾는 두 정점
    edges = list(map(int,input().split()))
    tree = [[] for _ in range(V+1)]

    for i in range(E):
        u, v = edges[i*2], edges[i*2+1]
        tree[u].append(v)

    visited = [0] * (V+1)
    global_path = []

    dfs(1,[],X)
    path_x = global_path[:]
    dfs(1,[],Y)
    path_y = global_path[:]
    print(path_x)
    print(path_y)
