import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 배열 입력받기 - 숫자를 문자열로 입력받아 2차원 배열 arr 만들기
    arr = []
    for _ in range(N):
        arr.append(input().split())
    # 결과 배열 만들고 arr과 같은 크기의 빈 문자열을 가진 2차원 배열로 만들기
    result = []
    for _ in range(N):
        result.append(['']*3)

    for i in range(N):
        for j in range(N):
            # 90도, 180도, 270도
            result[i][0] += arr[N-j-1][i]
            result[i][1] += arr[N-i-1][N-j-1]
            result[i][2] += arr[j][N-i-1]

    print("#{}".format(tc))
    for i in range(N):
        print('{}'.format(' '.join(result[i])))