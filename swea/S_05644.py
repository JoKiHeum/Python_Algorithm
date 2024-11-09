import sys
sys.stdin = open('S_05644.txt')

def charge(a_cur, b_cur):
    a_charge = []
    b_charge = []
    for i in range(BC):
        y, x, c, p = AP[i]
        if abs(a_cur[0] - y) + abs(a_cur[1] - x) <= c:
            a_charge.append((i, p))
        if abs(b_cur[0] - y) + abs(b_cur[1] - x) <= c:
            b_charge.append((i, p))

    return a_charge, b_charge


T = int(input())
for test_case in range(1,T+1):
    M, BC = map(int, input().split())       # M: 총 이동 시간, BC: 충전 갯수
    A = [0]+list(map(int,input().split()))      # A: A의 이동 경로
    B = [0]+list(map(int,input().split()))      # B: B의 이동 경로

    AP = []                                 # AP: 충전기 정보

    for _ in range(BC):
        x, y, c, p = map(int, input().split())
        AP.append([y-1, x-1, c, p])            # 좌표 계산하기 편하게 x,y 좌표에 -1 씩 해주기

    # a,b 현재 위치
    a_cur = (0,0)
    b_cur = (9,9)
    # 정지상우하좌
    dr = [0, -1, 0, 1, 0]
    dc = [0, 0, 1, 0, -1]
    # 총합
    total_sum = 0


    for i in range(M+1):
        # 위치 이동
        a_cur = (a_cur[0] + dr[A[i]], a_cur[1] + dc[A[i]])
        b_cur = (b_cur[0] + dr[B[i]], b_cur[1] + dc[B[i]])

        a_charge, b_charge = charge(a_cur, b_cur)
        max_charge = 0
        # 둘 다 충전소를 접속하는 경우 최대값 찾기

        for a_charge_num, a_power in a_charge:
            for b_charge_num, b_power in b_charge:
                if a_charge_num == b_charge_num:
                    power_charge = (a_power / 2) + (b_power / 2)
                else:
                    power_charge = a_power + b_power
                max_charge = max(max_charge, power_charge)
        # A만 있는 경우
        if not b_charge:
            for a_charge_num, a_power in a_charge:
                max_charge = max(max_charge, a_power)

        # B만 있는 경우
        if not a_charge:
            for b_charge_num, b_power in b_charge:
                max_charge = max(max_charge, b_power)



        total_sum += max_charge

    print(f'#{test_case} {int(total_sum)}')





