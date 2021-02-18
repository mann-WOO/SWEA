import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 괄호 문자열을 plan으로 입력받는다
    plan = input()
    # 현재 아래에 있는 쇠막대기 개수 current, 최종 쇠막대기 개수 total 초기화
    current = 0
    total = 0
    # 괄호 문자열을 하나씩 진행
    for i in range(len(plan)):
        # 여는 괄호라면 current에 1 합산
        if plan[i] == '(':
            current += 1
        # 닫는 괄호라면 current에 1 빼준다.
        else:
            current -= 1
            # 이번 닫는 것이 레이저 발사였다면, 현재 아래의 쇠막대기들이 한번 잘린다.
            # 따라서 currnet만큼 total에 합산
            if plan[i-1:i+1] == '()':
                total += current
            # 레이저 발사가 아닌 쇠막대기 끝이었다면 total에 남은 조각 1 합산
            else:
                total += 1

    print("#{} {}".format(tc, total))

