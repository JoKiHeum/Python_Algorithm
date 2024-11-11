import sys
sys.stdin = open('B_11657.txt')
# input = sys.stdin.readline

def bf(start):
    distance[start] = 0

    # 마지막 반복은 갱신이 일어나는지 안일어나는지 확인하기 위해서 진행
    for i in range(N):
        for start,end,time in edges:
            if distance[start] != float('inf') and distance[end] > distance[start]+ time:
                distance[end] = distance[start] + time
                if i == N-1:
                    return False
    return True




N, M = map(int,input().split())
edges = []
distance = [float('inf')] * (N+1)

for _ in range(M):
    start, end, time = map(int,input().split())
    edges.append((start,end,time))

result = bf(1)
if result:
    for i in range(2, N+1):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])

else:
    print(-1)

