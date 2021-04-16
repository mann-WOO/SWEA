import sys
sys.stdin = open("input.txt")


# 델타이동 방향
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 방 배열 입력
    rooms = []
    for _ in range(N):
        rooms.append(list(map(int, input().split())))
    # 각 방에서 다른 방으로 이동할 수 있는지 여부 체크하는 N^2 길이의 리스트 check
    check =[0 for x in range(N*N+1)]
    # check 리스트 입력
    for i in range(N):
        for j in range(N):
            # 각 방에서 네 방향 확인
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[i][j] + 1:
                    check[rooms[i][j]] = 1
                    break
    # 연속으로 이동가능한 방의 개수 세기 위한 cnt
    cnt = 1
    # cnt의 최댓값 max_cnt
    max_cnt = 1
    # max_cnt에서의 처음 방을 기록하는 max_num
    max_num = 0
    # check 리스트를 검토
    for i in range(1, N*N+1):
        # 다음 방으로 갈 수 있다면 cnt에 1 합산
        if check[i]:
            cnt += 1
        # 더 이상 갈 수 없다면 max_cnt와 비교해 max_cnt, max_num 갱신
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                # 첫 방의 숫자 구하기
                max_num = i - cnt + 1
            # cnt 초기화
            cnt = 1
    print("#{} {} {}".format(tc, max_num, max_cnt))

