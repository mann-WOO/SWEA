import sys
sys.stdin = open("input.txt")


# 사다리를 타고 내려가, 표시지점에 도착하면 첫 위치를, 아니면 False를 반환하는 함수 go_down
def go_down(arr, x):
    row = 0
    col = x
    # 사다리 시작점인지 확인
    if arr[row][col] == 0:
        return False
    # 맨 밑까지 내려가기 - 마지막에서 두번째 row까지 실행
    while row < 99:
        # 왼쪽 혹은 오른쪽으로 갈 수 있다면 갈 수 있는 만큼 이동
        # 왼쪽 확인
        if 0 <= col - 1 < 100 and arr[row][col - 1] == 1:
            # 갈 수 있는 만큼 이동
            while 0 <= col - 1 < 100 and arr[row][col - 1] == 1:
                col -= 1
        # 오른쪽 확인
        elif 0 <= col + 1 < 100 and arr[row][col + 1] == 1:
            # 갈 수 있는 만큼 이동
            while 0 <= col + 1 < 100 and arr[row][col + 1] == 1:
                col += 1
        # 아래 한칸 진행
        row += 1
    # 최종 도착점의 값이 2라면 x를 반환
    if arr[row][col] == 2:
        return x
    # 아니라면 False를 반환
    return False


T = 10
for tc in range(1, T+1):
    test_case = input()
    ladder = []
    # 사다리 생성
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
    # 결과 값을 담을 result 변수를 초기화
    result = False
    # 사다리의 모든 시작점에서 내려가는 작업을 반복
    for i in range(100):
        # 각 점에서 내려온 결과를 result에 할당
        result = go_down(ladder, i)
        # go_down 함수가 False가 아닌 값을 반환하면 종료
        if result:
            break

    print("#{} {}".format(tc, result))
