import sys
sys.stdin = open('B_11403.txt')

N = int(input())
distance = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    distance[i] = list(map(int, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][k] == 1 and distance[k][j] == 1:
                distance[i][j] = 1

for i in range(N):
    print(*distance[i])