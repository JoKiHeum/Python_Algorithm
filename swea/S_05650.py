import sys
sys.stdin = open('S_05650.txt')

def pinball(si, sj,d):
    global max_cnt
    ei, ej = si, sj
    cnt = 0
    while True:
        si += dr[d]
        sj += dc[d]
        if 0 <= si < N and 0 <= sj < N:
            # 출발점으로 돌아올 경우 또는 블랙홀에 들어갈 경우 종료
            if (si == ei and sj == ej) or (arr[si][sj] == -1):
                max_cnt = max(max_cnt, cnt)
                return
            # 웜홀을 만났을 때
            elif 6 <= arr[si][sj] <= 10:
                si, sj = wormhole[(si, sj)]
            # 블록을 만났을 때
            elif 1 <= arr[si][sj] <= 5:
                cnt += 1
                d = direction[arr[si][sj]][d]
        # 벽에 부딪혔을 때
        else:
            cnt += 1
            d = direction[5][d]

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 웜홀 순간이동 할 위치 저장
    tmp = dict()
    wormhole = dict()
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                if arr[i][j] in tmp:
                    wormhole[(i,j)] = tmp[arr[i][j]]
                    wormhole[tmp[arr[i][j]]] = (i,j)
                else:
                    tmp[arr[i][j]] = (i,j)

    # 방항 설정(상하좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    direction = [[],
                 [1, 3, 0, 2],      # 1번 블록: 상 -> 하, 하 -> 우, 좌 -> 상, 우 -> 좌
                 [3, 0, 1, 2],       # 2번 블록: 상 -> 우, 하 -> 상, 좌 -> 하, 우 -> 좌
                 [2, 0, 3, 1],
                 [1, 2, 3, 0],
                 [1, 0, 3, 2]]

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for d in range(4):
                    pinball(i, j, d)

    print(f'#{test_case} {max_cnt}')
