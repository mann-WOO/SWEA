import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 델타 이동
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    # 보드의 크기 N, 플레이 수 M
    N, M = map(int, input().split())
    board = [[0]*N for i in range(N)]
    # 가운데 돌 4개 채워주기
    c = int(N/2) - 1
    board[c][c], board[c+1][c+1] = 2, 2
    board[c+1][c], board[c][c+1] = 1, 1
    # 모든 플레이에 대해
    for _ in range(M):
        col, row, color = map(int, input(). split())
        # 행렬 인덱스에 맞게 조정
        row -= 1
        col -= 1
        # 이번 플레이에 놓은 위치의 돌 색 지정
        board[row][col] = color
        # 델타이동
        for i in range(8):
            # 현재 지점 설정
            current_row = row
            current_col = col
            stack = []
            # 다음 진행 지점에 접근 가능할때까지 진행
            while 0 <= current_row+dr[i] < N and 0 <= current_col+dc[i] < N:
                # 현재지점 갱신
                current_row = current_row+dr[i]
                current_col = current_col+dc[i]
                # 빈칸인 경우 다음 델타 이동
                if board[current_row][current_col] == 0:
                    break
                # 다른 색인 경우 stack에 현재 위치 추가
                elif board[current_row][current_col] != color:
                    stack.append((current_row, current_col))
                # 같은 색인 경우 stack의 점들을 color로 바꿔주고 다음 델타 이동
                else:
                    while stack:
                        change_row, change_col = stack.pop()
                        board[change_row][change_col] = color
                    break
    # 돌 개수 세기
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print("#{} {} {}".format(tc, black, white))

