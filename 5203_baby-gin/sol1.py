import sys
sys.stdin = open("input.txt")


# run 판별 함수
def is_run(player):
    for i in range(10):
        if player[i] != 0:
            cnt = 1
            current = i
            while current < 9:
                current += 1
                if player[current] != 0:
                    cnt += 1
                    if cnt == 3:
                        return True
                else:
                    break


# triplet 판별 함수
def is_triplet(player):
    for i in range(10):
        if player[i] == 3:
            return True


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    # 숫자 갯수 기록 리스트 player1, player2
    player1 = [0 for x in range(10)]
    player2 = [0 for x in range(10)]
    # 처음 두장 가지기
    for _ in range(2):
        player1[numbers.pop(0)] += 1
        player2[numbers.pop(0)] += 1
    # 세 번째 카드부터 승부 진행, 결과 기본값 0(무승부)
    result = 0
    # 카드가 다 떨어질때까지 반복
    while numbers:
        # 플레이어1, 2가 번갈아가며 카드 한 장 가지고 run, triplet 여부 판별 후 result 갱신
        player1[numbers.pop(0)] += 1
        if is_run(player1) or is_triplet(player1):
            result = 1
            break
        player2[numbers.pop(0)] += 1
        if is_run(player2) or is_triplet(player2):
            result = 2
            break
    print("#{} {}".format(tc, result))

