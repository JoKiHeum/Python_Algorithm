import sys
sys.stdin = open('S_05650.txt')

T = int(input())
for test_cast in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    