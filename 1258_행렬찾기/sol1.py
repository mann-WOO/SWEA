import sys
sys.stdin = open("input.txt")


# find, change, out: 0이 아닌 점을 만나면 시행
def fco(arr, row, col):
    # find: 오른쪽 끝, 아래 끝까지의 거리를 찾아낸다
    nr = row
    nc = col
    row_len = 1
    col_len = 1
    while 0 <= nc + 1 < N and arr[nr][nc+1] != 0:
        nc += 1
        col_len += 1
    while 0 <= nr + 1 < N and arr[nr+1][nc] != 0:
        nr += 1
        row_len += 1
    # change: 찾은 영역을 0으로 만들어준다
    for i in range(row, row + row_len):
        for j in range(col, col + col_len):
            arr[i][j] = 0
    # out: 행, 열의 길이를 반환한다.
    return row_len, col_len


T = int(input())
for tc in range(1, T+1):
    # 행렬의 크기 NxN
    N = int(input())
    # 행렬 입력받기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # sub matrix의 길이를 담을 리스트 result
    result = []
    # 모든 점을 검토하며 0이 아닐경우 fco를 시행
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                result.append(fco(arr, i, j))
    # result를 정렬
    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    # 출력
    print("#{}".format(tc), end=' ')
    print(len(result), end=' ')
    for i in range(len(result)):
        print('{}'.format(' '.join(map(str, result[i]))), end=' ')
    print()


