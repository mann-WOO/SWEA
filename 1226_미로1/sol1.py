import sys
sys.stdin = open("input.txt")


# 델타이동 리스트
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 시작점을 찾는 함수
def find_start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j


# dfs
def dfs(maze, start):
    # stack, 방문기록 visited 초기화
    stack = [start]
    visited = [[0]*16 for _ in range(16)]
    visited[start[0]][start[1]] = 1
    while stack:
        # 스택에서 꺼낸 현재 위치 확인
        current_row, current_col = stack.pop()
        # 네 방향에 대해
        for i in range(4):
            # 나아간 방향의 좌표 nr nc
            nr = current_row + dr[i]
            nc = current_col + dc[i]
            # 벽이 아니고 방문하지 않았다면
            if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                # 도착점일 때 1을 출력하고 끝냄
                if maze[nr][nc] == 3:
                    return 1
                # 도착점이 아니면 방문(예정)기록 남기고 스택에 좌표 추가
                else:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))
    # 모두 탐색했으나 못찾으면 0 반환
    return 0


# bfs
def bfs(maze, start):
    # 큐, 방문기록 visited 초기화
    q = [start]
    visited = [[0] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = 1
    while q:
        # 스택에서 꺼낸 현재 위치 확인
        current_row, current_col = q.pop(0)
        # 네 방향에 대해
        for i in range(4):
            nr = current_row + dr[i]
            nc = current_col + dc[i]
            # 벽이 아니고 방문하지 않았다면
            if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                # 도착점일 경우 1 출력 후 종료
                if maze[nr][nc] == 3:
                    return 1
                else:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
    # 모두 탐색했으나 못찾으면 0 반환
    return 0


T = 10
for tc in range(1, T+1):
    test_case = input()
    # 미로 입력받기
    maze = []
    for _ in range(16):
        maze.append(list(map(int, list(input()))))
    # 시작점 찾기
    start = find_start(maze)
    print("#{} {}".format(tc, dfs(maze, start)))

