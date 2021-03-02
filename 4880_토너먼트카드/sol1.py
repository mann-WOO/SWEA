import sys
sys.stdin = open("input.txt")

# enumerate 된 tuple을 인자로 받아 가위바위보 게임의 승자를 반환하는 winner
def winner(a, b):
    if a[1] == 1:
        if b[1] == 1:
            return a
        if b[1] == 2:
            return b
        if b[1] == 3:
            return a
    if a[1] == 2:
        if b[1] == 1:
            return a
        if b[1] == 2:
            return a
        if b[1] == 3:
            return b
    if a[1] == 3:
        if b[1] == 1:
            return b
        if b[1] == 2:
            return a
        if b[1] == 3:
            return a


# 토너먼트를 진행하는 tournament
def tournament(arr):
    # 길이가 1인 배열을 입력받으면 유일한 원소를 반환
    if len(arr) == 1:
        return arr[0]
    # 길이가 2인 배열을 입력받으면 승자 원소를 반환
    elif len(arr) == 2:
        return winner(arr[0], arr[1])
    # 길이가 3 이상인 배열을 입력받으면 반으로 나누고 토너먼트를 진행해 승자를 반환
    else:
        mid = (1+len(arr))//2
        return winner(tournament(arr[:mid]), tournament(arr[mid:]))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 카드 입력
    cards = list(map(int, input().split()))
    # 학생 번호와 카드를 튜플로 묶어줌
    student_card = []
    for i in range(N):
        student_card.append((i+1, cards[i]))
    # (승자번호, 카드)의 튜플 result
    result = tournament(student_card)

    print("#{} {}".format(tc, result[0]))
