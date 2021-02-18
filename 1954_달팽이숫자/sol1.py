T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N*N의 arr 생성
    arr = []
    for _ in range(N):
        arr.append(N * [0])
    # 1씩 더해가며 원소에 부여할 cnt 선언
    cnt = 1
    # (0,0)부터 대각선 아래방향으로 가면서 한 바퀴씩 돈다.
    for i in range((N+1) // 2):
        col = i
        row = i
        # 오른쪽으로 진행하며 끝점, 혹은 이미 숫자가 부여된 점까지 진행
        while col + 1 < N and arr[row][col+1] == 0:
            arr[row][col] = cnt
            cnt += 1
            col += 1
        # 아래쪽으로
        while row + 1 < N and arr[row+1][col] == 0:
            arr[row][col] = cnt
            cnt += 1
            row += 1
        # 왼쪽으로
        while col -1 > -1 and arr[row][col-1] == 0:
            arr[row][col] = cnt
            cnt += 1
            col -= 1
        # 위로
        while row -1 > -1 and arr[row-1][col] == 0:
            arr[row][col] = cnt
            cnt += 1
            row -= 1
        # 마지막 점에 숫자 부여
        arr[row][col] = cnt
        cnt += 1

    # output을 위해 arr를 문자열로 변환
    result = ''
    for i in range(N):
        for j in range(N):
            result += f'{arr[i][j]} '
        result = result.strip()
        result += '\n'
    print('#{}\n{}'.format(tc, result.strip()))
