import sys
sys.stdin = open('B_01516.txt')
from collections import deque

def topology_sort():
    build_time_sum = [0] * (N+1)
    q = deque()

    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        for w in G[v]:
            indegree[w] -= 1
            build_time_sum[w] = max(build_time_sum[w], build_time_sum[v]+build_time[v])
            if indegree[w] == 0:
                q.append(w)
    return build_time_sum

N = int(input())
G = [[] for _ in range(N+1)]            # 인접리스트
indegree = [0] * (N+1)                  # 진입 차수
build_time = [0] * (N+1)                # 건물 짓는데 걸리는 시간

for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    build_time[i] = tmp[0]
    for j in range(1,len(tmp)):
        if tmp[j] == -1:
            break
        else:
            G[tmp[j]].append(i)
            indegree[i] += 1

result = topology_sort()

for i in range(1,N+1):
    print(result[i]+build_time[i])
