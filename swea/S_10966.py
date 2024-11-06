import sys
sys.stdin = open('S_10966.txt')
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs():
    result = 0
    while q:
        r,c = q.popleft()


        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
                result += visited[r][c] + 1
    return result



T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    q = deque()
    visited = [[-1] * M for _ in range(N)]

    total = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 0
    result = bfs()

    print(f'#{test_case} {result}')

