import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 각 날의 매매가 N
    price = list(map(int, input().split()))
    # 수익을 기록할 profits 초기화
    profits = 0
    # 마지막 날의 값을 판매가로 초기화
    sell_price = price[N-1]
    # 뒤에서 부터 거꾸로 하나씩 확인
    for i in range(N-2, -1, -1):
        # 가격이 판매가보다 낮다면 수익에 그 차를 추가
        if price[i] < sell_price:
            profits += sell_price-price[i]
        # 가격이 판매가보다 높다면 판매가를 갱신
        else:
            sell_price = price[i]

    print("#{} {}".format(tc, profits))

