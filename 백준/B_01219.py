"""
도착 할 수 없을 때: gg
돈을 무한히 가질 수 있을 때: GEE
"""
def df(s):
    D[s] = -money[s]

    for i in range(N-1):
        for start,end,cost in edges:
            if D[start] != float('inf') and D[end] > D[start] + cost:
                D[end] = D[start] + cost
                if i == N-2:            # 돈을 무한히 가질 수 있을 경우
                    return False
    return True


import sys
sys.stdin = open('B_01219.txt')

N, S, E, M = map(int,input().split())   # N: 도시의 수, S: 시작도시, E: 종료도시, M: 간선의 수
D = [float('inf')] * N                  # 거리 정보
edges = []

for _ in range(M):
    u, v, cost = map(int,input().split())
    edges.append([u,v,cost])

money = list(map(int,input().split()))


# 비용 업데이트
for i in range(M):
    tmp_cost = money[edges[i][1]]
    edges[i][2] -= tmp_cost




result = df(S)
# 만약 돈을 무한히 벌경우
if not result:
    if D[E] != float('inf'):
        print('Gee')
    else:
        print('gg')
else:
    if D[E] == float('inf'):
        print('gg')
    else:
        print(-D[E])

