import sys
sys.stdin = open("input.txt")

T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for tc in range(1, T+1):
    N = int(input())
    maze = []
    # 미로 입력받기
    for i in range(N):
        maze.append(list(map(int, list(input()))))

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    # stack 초기화 하고 시작점 추가하기
    stack = [start]

    # 결과값 기본 0(불가능)
    result = 0
    # 탐색, stack을 비울 때까지
    while stack:
        # stack 에서 꺼내 현재 지점으로 설정
        current_row, current_col = stack.pop()
        # 현재 지점을 벽으로 만들어줌
        maze[current_row][current_col] = 1
        # 현재 지점에서 진출 가능 방향을 탐색
        for i in range(4):
            if 0 <= current_row + dr[i] < N and 0 <= current_col + dc[i] < N and maze[current_row + dr[i]][current_col + dc[i]] != 1:
                # 진출 가능 지점이 도착점이라면 스택을 비우고 break
                if maze[current_row + dr[i]][current_col + dc[i]] == 3:
                    result = 1
                    stack = []
                    break
                else:
                    stack.append((current_row + dr[i], current_col + dc[i]))

    print("#{} {}".format(tc, result))


