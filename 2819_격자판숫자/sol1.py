import sys
sys.stdin = open("input.txt")


# 델타이동 방향
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


# 여섯 번 움직인 결과를 result에 추가하는 함수
def move_six(i, j, number_string, cnt):
    # cnt(문자열 길이)가 7이 되면 결과 리스트에 추가
    if cnt == 7:
        result.append(int(number_string))
    # 문자열 길이가 7 미만인 경우
    else:
        # 네 방향 탐색
        for d in range(4):
            # 진행 가능한 경우
            if 0 <= i + dr[d] < 4 and 0 <= j + dc[d] < 4:
                # 문자열 개수에 1 합산
                cnt += 1
                # 진행하는 방향의 수를 문자열에 추가
                number_string += str(board[i+dr[d]][j+dc[d]])
                # 다음 탐색
                move_six(i+dr[d], j+dc[d], number_string, cnt)
                # 문자열 개수 1 빼주기
                cnt -= 1
                # 마지막 문자 제외시켜주기
                number_string = number_string[:cnt]


T = int(input())
for tc in range(1, T+1):
    # 격자판 입력받기
    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))
    # 결과리스트
    result = []
    # 모든 점에 대해 문자열 생성
    for i in range(4):
        for j in range(4):
            number_string = str(board[i][j])
            cnt = 1
            move_six(i, j, number_string, cnt)
    # set으로 중복 제거하여 숫자의 개수 출력
    print("#{} {}".format(tc, len(set(result))))

