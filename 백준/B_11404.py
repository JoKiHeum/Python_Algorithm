import sys
sys.stdin = open('B_11404.txt')

N = int(input())
M = int(input())

# 인접행렬 생성 및 초기화
arr = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    u, v, w = map(int,input().split())
    if arr[u-1][v-1] > w:
        arr[u-1][v-1] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(N):
    for j in range(N):
        if arr[i][j] == float('inf'):
            arr[i][j] = 0

for i in range(N):
    print(*arr[i])

