import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 오븐의 크기 N, 피자의 개수 M
    N, M = map(int, input().split())
    # 피자에 번호 부여하여 리스트로 만들기
    pizza_nums = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        pizza.append([i+1, pizza_nums[i]])
    # 오븐과 피자를 초기화
    oven, pizza = pizza[:N], pizza[N:]
    # 오븐에서 나온 가장 최근 피자 out 초기화
    out = [0, 0]
    # 오븐을 비울 때까지 반복
    while oven:
        # oven에서 pop(0)하여 tmp로
        tmp = oven.pop(0)
        # 치즈양 반으로 줄이기
        tmp = [tmp[0], tmp[1]//2]
        # 치즈가 0 이 될 때
        if tmp[1] == 0:
            # pizza가 남아있다면 pizza에서 pop(0)한 원소를 oven 에 추가
            if pizza:
                oven.append(pizza.pop(0))
            # pizza 추가 여부와 관계 없이 out을 tmp로 갱신
            out = tmp
        # 치즈가 0이 아니라면 오븐에 추가
        else:
            oven.append(tmp)
    print("#{} {}".format(tc, out[0]))

