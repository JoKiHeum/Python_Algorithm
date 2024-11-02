import sys
sys.stdin = open('B_02660.txt')

N = int(input())
arr = [[N] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            arr[i][j] = 0

while True:
    u,v = map(int, input().split())
    if u == -1 and v == -1:
        break
    arr[u-1][v-1], arr[v-1][u-1] = 1, 1

for k in range(N):                  # 중간 경로
    for i in range(N):              # 시작
        for j in range(N):          # 끝
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

dist = [0] * N
for i in range(N):
    dist[i] = max(arr[i])

tmp = min(dist)
answer = []
cnt = 0
for i in range(N):
    if dist[i] == tmp:
        cnt += 1
        answer.append(i+1)

print(tmp, cnt)
print(*answer)


