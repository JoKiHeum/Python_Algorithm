import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    for _ in range(M):
        i,j = map(int,input().split())
        for k in range(1,j+1):
            if 0 <= i-1-k and i-1+k < N:
                if arr[i-1-k] == 0 and arr[i-1-k] == arr[i-1+k]:
                    arr[i-1-k] = arr[i-1+k] =1
                elif arr[i-1-k] == 1 and arr[i-1-k] == arr[i-1+k]:
                    arr[i-1 - k] = arr[i-1 + k] = 0
    print(f'#{test_case}', end = ' ')
    print(*arr)

