import sys
sys.stdin = open("input.txt")


# 일반항 f(n) = 2*f(n-2) + f(n-1)
def paper(n, arr):
    arr[0] = 1
    arr[1] = 3
    for i in range(2, n):
        arr[i] = (2 * arr[i-2]) + arr[i-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = int(N/10)
    # 일반항을 이용해 n번째 원소를 구함
    arr = [0] * n
    paper(n, arr)

    print("#{} {}".format(tc, arr[n-1]))
