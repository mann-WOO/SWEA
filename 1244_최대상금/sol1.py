import sys
sys.stdin = open("input.txt")


# 순열 생성해 최댓값 저장 함수
def f(i, n, cnt):
    global maxV
    global maxC
    # 자리를 다 바꿨거나 순서 교환 횟수 모두 사용 시
    if i == n or cnt == 0:
        s = 0
        # cards를 int로 만들기
        for k in range(n):
            s = s*10 + int(cards[k])
        # maxV와 s 비교해서 maxV, maxC 갱신하기
        if maxV <= s:
            maxV = s
            if maxC > cnt:
                maxC = cnt
    # 자리 바꿔주고 제자리 교환이 아닌 경우 cnt 1씩 줄이기
    else:
        for j in range(i, n):
            cards[i], cards[j] = cards[j], cards[i]
            c = 0 if i == j else 1
            f(i+1, n, cnt-c)
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for tc in range(1, T+1):
    cards, N = input().split()
    cards = list(cards)
    maxV = 0
    cnt = int(N)
    maxC = cnt
    f(0, len(cards), cnt)
    # 교환 횟수가 홀수로 남았고
    if maxC % 2:
        # 겹치는 숫자가 없을 때
        if len(list(str(maxV))) == len(set(str(maxV))):
            # 마지막 자리수
            one = maxV % 10
            # 마지막 두번째 자리수
            ten = int(((maxV % 100) - one) / 10)
            # 차이 계산
            diff = (ten * 10 + one) - (one * 10 + ten)
            # maxV에서 차이 빼주기
            maxV = maxV - diff
    print("#{} {}".format(tc, maxV))

