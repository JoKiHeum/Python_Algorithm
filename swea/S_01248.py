import sys
sys.stdin = open('S_01248.txt')
from collections import deque
# DFS를 활용한 길 찾기
def dfs1(v,path,target):
    global global_path_1
    visited_1[v] = 1
    path.append(v)
    if v == target:
        global_path_1 = path[:]

    for w in tree[v]:
        if not visited_1[w]:
            dfs1(w,path,target)
            path.pop()

def dfs2(v,path,target):
    global global_path_2
    visited_2[v] = 1
    path.append(v)
    if v == target:
        global_path_2 = path[:]

    for w in tree[v]:
        if not visited_2[w]:
            dfs2(w,path,target)
            path.pop()

# 서브트리 크기 구하기
def bfs(s):
    visited = [0] * (V+1)
    visited[s] = 1
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()
        visited[v] = 1
        for w in tree[v]:
            if not visited[w]:
                q.append(w)
    return visited
T = int(input())
for test_case in range(1,T+1):
    V, E, X, Y = map(int,input().split())       # V: 정점의 수, E: 간선의 수, X,Y: 공통조상을 찾는 두 정점
    edges = list(map(int,input().split()))
    tree = [[] for _ in range(V+1)]

    for i in range(E):
        u, v = edges[i*2], edges[i*2+1]
        tree[u].append(v)

    visited_1 = [0] * (V+1)
    visited_2 = [0] * (V+1)

    global_path_1 = []
    global_path_2 = []
    dfs1(1,[],X)
    dfs2(1,[],Y)

    for i in range(len(global_path_1)-1,-1,-1):
        if global_path_1[i] in global_path_2:
            index = i
            break
    same_parent = global_path_1[index]

    result = bfs(same_parent)
    print(f'#{test_case} {same_parent} {sum(result)}')
