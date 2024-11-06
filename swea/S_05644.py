import sys
sys.stdin = open('S_05644.txt')

T = int(input())
for test_case in range(1,T+1):
    M, BC = map(int, input().split())       # M: 총 이동 시간, BC: 충전 갯수
    A = list(map(int,input().split()))      # A: A의 이동 경로
    B = list(map(int,input().split()))      # B: B의 이동 경로

    AP = [0 for _ in range(BC)]                                 # AP: 충전기 정보

    for i in range(BC):
        x, y, c, p = map(int, input().split())
        AP[i] = [y-1, x-1, c, p]            # 좌표 계산하기 편하게 x,y 좌표에 -1 씩 해주기

    